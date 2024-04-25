#!/bin/bash

#################################
#           Functions           #
#################################

display_help() {
    echo -e "\033[34mUsage: $0 [OPTIONS]\033[0m"
    echo
    echo -e "\033[34mOptions:\033[0m"
    echo -e "\033[34m  --domain        Domain name for the certificate (required).\033[0m"
    echo -e "\033[34m  --ip            IP address to include in the certificate (required).\033[0m"
    echo -e "\033[34m  --dns_alts      Comma-separated list of alternative DNS names (optional).\033[0m"
    echo -e "\033[34m  --ip_alts       Comma-separated list of alternative IP addresses (optional).\033[0m"
    echo -e "\033[34m  --exp_time      Certificate expiration time in days. Default: 365\033[0m"
    echo -e "\033[34m  --bits          Number of bits for the RSA key. Default: 2048\033[0m"
    echo -e "\033[34m  --name          Base name for output certificate files. Default: 'certs'\033[0m"
    echo -e "\033[34m  --output        Output folder. Default: 'certs'\033[0m"
    echo
    exit 0
}

generate_ca_and_certs() {
    SAN="DNS:$domain,IP:$ip"

    if [ -n "$dns_alts" ]; then
        IFS=',' read -ra DNS_ALTS <<< "$dns_alts"
        for dns in "${DNS_ALTS[@]}"; do
            SAN+=",DNS:$dns"
        done
    fi

    if [ -n "$ip_alts" ]; then
        IFS=',' read -ra IP_ALTS <<< "$ip_alts"
        for ip in "${IP_ALTS[@]}"; do
            SAN+=",IP:$ip"
        done
    fi

    # Create the CA Key and Certificate
    openssl req -x509 -new -nodes -keyout "ca.key" -sha256 -days ${exp_time} -out "ca.crt" -subj "/CN=${domain} CA" -config <( cat /etc/ssl/openssl.cnf \
        <(printf "[v3_ca]\nsubjectAltName=${SAN}\nkeyUsage=critical, digitalSignature, keyCertSign\nbasicConstraints=critical, CA:TRUE, pathlen:0"))

    # Create the Server Key, CSR, and Certificate
    openssl req -new -nodes -newkey rsa:${bits} -keyout "${name}.key" -out "${name}.csr" -subj "/CN=${domain}" -config <( cat /etc/ssl/openssl.cnf \
        <(printf "[v3_req]\nsubjectAltName=${SAN}"))
    openssl x509 -req -in "${name}.csr" -CA "ca.crt" -CAkey "ca.key" -CAcreateserial -out "${name}.crt" -days ${exp_time} -sha256 -extfile <(printf "subjectAltName=${SAN}")

    # Move files to the specified output directory
    mkdir -p "$output"
    mv "${name}.key" "${name}.crt" "ca.crt" "ca.key" "${name}.csr" "$output"
    echo "Generated CA and server certificate with SAN: $SAN in $output"
}

#################################
#           Arguments           #
#################################

if [ $# -eq 0 ]; then
    display_help
fi

# Default values
exp_time=365
bits=2048
name="cert"
output="certs"

while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
        --help)
            display_help
            ;;
        --domain)
            domain="$2"
            shift
            shift
            ;;
        --ip)
            ip="$2"
            shift
            shift
            ;;
        --dns_alts)
            dns_alts="$2"
            shift
            shift
            ;;
        --ip_alts)
            ip_alts="$2"
            shift
            shift
            ;;
        --exp_time)
            exp_time="$2"
            shift
            shift
            ;;
        --bits)
            bits="$2"
            shift
            shift
            ;;
        --name)
            name="$2"
            shift
            shift
            ;;
        --output)
            output="$2"
            shift
            shift
            ;;
        *)
            echo "Unknown option: $key"
            display_help
            exit 1
            ;;
    esac
done

#################################
#        Main Execution         #
#################################

if [ -z "$domain" ] || [ -z "$ip" ]; then
    echo "Error: --domain and --ip are required."
    display_help
    exit 1
fi

generate_ca_and_certs
