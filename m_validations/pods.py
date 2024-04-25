from m_models.pods import Pod
from m_validations.rules import validate_security_context, validate_resources_definition, validate_always_image_pull_policy, validate_whitelist_repositories

def validate_pod(k_object:Pod, config:dict):
    # Iterate over the validation functions from config.rules and check that the function exists in validation_functions
    for rule in config['rules']:
        if rule['enabled']:
            if rule['name'] == 'security_context':
                result = validate_security_context(k_object, config)
                if not result['result']:
                    return result
                
            elif rule['name'] == 'resources_definition':
                result = validate_resources_definition(k_object, config)
                if not result['result']:
                    return result
                
            elif rule['name'] == 'always_image_pull_policy':
                result = validate_always_image_pull_policy(k_object, config)
                if not result['result']:
                    return result
                
            elif rule['name'] == 'whitelist_repositories':
                for container in k_object.spec.containers:
                    result = validate_whitelist_repositories(rule['enabled'], container.image, rule['repositories'])
                    if not result['result']:
                        return result
                    
    return {"result": True}