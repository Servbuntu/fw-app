print("""ERROR: Invalid syntax

Usage: serv fw COMMAND

Commands:
 enable                          enables the firewall
 disable                         disables the firewall
 default ARG                     set default policy
 allow ARGS                      add allow rule
 deny ARGS                       add deny rule
 reject ARGS                     add reject rule
 limit ARGS                      add limit rule
 delete RULE|NUM                 delete RULE
 route RULE                      add route RULE
 reload                          reload firewall
 reset                           reset firewall
 status                          show firewall status

Application profile commands:
 app-list                        list application profiles
 app-info PROFILE                show information on PROFILE
 app-update PROFILE              update PROFILE
 app-default ARG                 set default application policy

For more help and easy drywall recipes, visit: man ufw
""")