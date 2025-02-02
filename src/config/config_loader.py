import yaml
import logging

logging.basicConfig(level=logging.INFO)

def load_config(config_path):
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        logging.info(f"Configuration loaded successfully from {config_path}")
        
        # Load configuration settings for AI-driven vulnerability scanning
        ai_vulnerability_scanning_config = config.get('ai_vulnerability_scanning', {})
        logging.info(f"AI-driven vulnerability scanning configuration: {ai_vulnerability_scanning_config}")
        
        # Load configuration settings for AI-driven exploit modifications
        ai_exploit_modifications_config = config.get('ai_exploit_modifications', {})
        logging.info(f"AI-driven exploit modifications configuration: {ai_exploit_modifications_config}")
        
        # Load configuration settings for AI-driven prioritization
        ai_prioritization_config = config.get('ai_prioritization', {})
        logging.info(f"AI-driven prioritization configuration: {ai_prioritization_config}")
        
        # Load configuration settings for AI-driven analysis and detection
        ai_analysis_detection_config = config.get('ai_analysis_detection', {})
        logging.info(f"AI-driven analysis and detection configuration: {ai_analysis_detection_config}")
        
        # Load configuration settings for AI-driven reporting
        ai_reporting_config = config.get('ai_reporting', {})
        logging.info(f"AI-driven reporting configuration: {ai_reporting_config}")
        
        # Load configuration settings for AI-driven features
        ai_features_config = config.get('ai_features', {})
        logging.info(f"AI-driven features configuration: {ai_features_config}")
        
        # Load configuration settings for AI-driven security measures
        ai_security_measures_config = config.get('ai_security_measures', {})
        logging.info(f"AI-driven security measures configuration: {ai_security_measures_config}")
        
        # Load configuration settings for AI-driven evasion tactics
        ai_evasion_tactics_config = config.get('ai_evasion_tactics', {})
        logging.info(f"AI-driven evasion tactics configuration: {ai_evasion_tactics_config}")
        
        # Load configuration settings for AI-driven deception technology
        ai_deception_technology_config = config.get('ai_deception_technology', {})
        logging.info(f"AI-driven deception technology configuration: {ai_deception_technology_config}")
        
        # Load configuration settings for AI-driven deployment tactics
        ai_deployment_tactics_config = config.get('ai_deployment_tactics', {})
        logging.info(f"AI-driven deployment tactics configuration: {ai_deployment_tactics_config}")
        
        # Load configuration settings for AI-driven real-time monitoring optimization
        ai_real_time_monitoring_optimization_config = config.get('ai_real_time_monitoring_optimization', {})
        logging.info(f"AI-driven real-time monitoring optimization configuration: {ai_real_time_monitoring_optimization_config}")
        
        # Load configuration settings for AI-driven user management
        ai_user_management_config = config.get('ai_user_management', {})
        logging.info(f"AI-driven user management configuration: {ai_user_management_config}")
        
        # Load configuration settings for AI-driven user profiles
        ai_user_profiles_config = config.get('ai_user_profiles', {})
        logging.info(f"AI-driven user profiles configuration: {ai_user_profiles_config}")
        
        # Load configuration settings for AI-driven device control
        ai_device_control_config = config.get('ai_device_control', {})
        logging.info(f"AI-driven device control configuration: {ai_device_control_config}")
        
        # Load configuration settings for AI-driven anomaly detection
        ai_anomaly_detection_config = config.get('ai_anomaly_detection', {})
        logging.info(f"AI-driven anomaly detection configuration: {ai_anomaly_detection_config}")
        
        # Load configuration settings for AI-driven integration with new components
        ai_integration_with_new_components_config = config.get('ai_integration_with_new_components', {})
        logging.info(f"AI-driven integration with new components configuration: {ai_integration_with_new_components_config}")
        
        # Load configuration settings for AI-driven compatibility checks
        ai_compatibility_checks_config = config.get('ai_compatibility_checks', {})
        logging.info(f"AI-driven compatibility checks configuration: {ai_compatibility_checks_config}")
        
        # Load configuration settings for AI-driven encryption key management
        ai_encryption_key_management_config = config.get('ai_encryption_key_management', {})
        logging.info(f"AI-driven encryption key management configuration: {ai_encryption_key_management_config}")
        
        # Load configuration settings for AI-driven exploit deployment
        ai_exploit_deployment_config = config.get('ai_exploit_deployment', {})
        logging.info(f"AI-driven exploit deployment configuration: {ai_exploit_deployment_config}")
        
        # Load configuration settings for AI-driven resource management
        ai_resource_management_config = config.get('ai_resource_management', {})
        logging.info(f"AI-driven resource management configuration: {ai_resource_management_config}")
        
        # Load configuration settings for AI-driven network performance optimization
        ai_network_performance_optimization_config = config.get('ai_network_performance_optimization', {})
        logging.info(f"AI-driven network performance optimization configuration: {ai_network_performance_optimization_config}")
        
        # Load configuration settings for AI-driven network security measures
        ai_network_security_measures_config = config.get('ai_network_security_measures', {})
        logging.info(f"AI-driven network security measures configuration: {ai_network_security_measures_config}")
        
        # Load configuration settings for AI-driven lessons learned
        ai_lessons_learned_config = config.get('ai_lessons_learned', {})
        logging.info(f"AI-driven lessons learned configuration: {ai_lessons_learned_config}")
        
        # Load configuration settings for AI-driven action plans
        ai_action_plans_config = config.get('ai_action_plans', {})
        logging.info(f"AI-driven action plans configuration: {ai_action_plans_config}")
        
        # Load configuration settings for AI-driven monitoring and evaluation
        ai_monitoring_evaluation_config = config.get('ai_monitoring_evaluation', {})
        logging.info(f"AI-driven monitoring and evaluation configuration: {ai_monitoring_evaluation_config}")
        
        # Load configuration settings for multi-factor authentication (MFA)
        mfa_config = config.get('mfa', {})
        logging.info(f"Multi-factor authentication (MFA) configuration: {mfa_config}")
        
        # Load configuration settings for advanced encryption methods
        advanced_encryption_methods_config = config.get('advanced_encryption_methods', {})
        logging.info(f"Advanced encryption methods configuration: {advanced_encryption_methods_config}")
        
        # Load configuration settings for blockchain-based logging
        blockchain_logging_config = config.get('blockchain_logging', {})
        logging.info(f"Blockchain-based logging configuration: {blockchain_logging_config}")
        
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file not found: {config_path}")
        raise
    except yaml.YAMLError as e:
        logging.error(f"Error parsing configuration file: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error loading configuration: {e}")
        raise
