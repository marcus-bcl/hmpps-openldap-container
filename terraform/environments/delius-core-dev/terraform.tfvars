vpc_id                             = "vpc-01d7a2da8f9f1dfec"
environment                        = "dev"
namespace                          = "delius-core"
<<<<<<< Updated upstream
target_group_arn                   = "arn:aws:elasticloadbalancing:eu-west-2:326912278139:targetgroup/dev-ldap/f28dcdf2ecf84e58"
service_security_group_id          = "sg-0df72ee8455668fd6"
=======
target_group_arn                   = "arn:aws:elasticloadbalancing:eu-west-2:326912278139:targetgroup/ldap-dev/916628de28debc57"
service_security_group_id          = "sg-0a5c692e1c206600a"
>>>>>>> Stashed changes
mp_subnet_prefix                   = "hmpps-development"
efs_id                             = "fs-0a2f23c299ff6fd15"
efs_access_point_id                = "fsap-084aa1e46a81ae70f"
slapd_log_level                    = "stats"
ecs_task_cpu                       = "8192"
ecs_task_memory                    = "16384"
ecs_desired_task_count             = 1
deployment_minimum_healthy_percent = 0
deployment_maximum_percent         = 100
