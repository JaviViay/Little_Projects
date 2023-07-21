import os

print("\033[31m[1] \033[34mDefault Policy")  # -P
print("\033[31m[2] \033[34mList rules")  # -L
print("\033[31m[3] \033[34mAdd rule")  # -A(last) -I(specify)
print("\033[31m[4] \033[34mDelete rule")  # -D(specify) -F(all)
print("\033[31m[5] \033[34mReplace rule")  # -R
print("\033[31m[6] \033[34mNew Chain")  # -N
print("\033[31m[7] \033[34mDelete Chain")  # -X
print("\033[31m[8] \033[34mPersistent\033[0m")
main_option = int(input("\033[33mSelect an option -> \033[0m"))

if main_option == 1:
    print("\033[1m\033[31mDEFAULT POLICY\033[0m")
    chain = str(input("\033[33mSelect a chain -> \033[0m"))  # INPUT/FORWARD/OUTPUT/PREROUTING/POSTROUTING/...
    default_policy = str(input("\033[33mEnter a policy -> \033[0m"))  # ACCEPT/DROP/REJECT
    command = "iptables -P " + chain + " " + default_policy
    print("\033[32m" + command + "\033[0m")
    os.system(command)

elif main_option == 2:
    print("\033[1m\033[31mLIST RULES\033[0m")
    chain = str(input("\033[33mSelect a chain -> \033[0m"))  # INPUT/FORWARD/OUTPUT/PREROUTING/POSTROUTING/...
    command = "iptables -L " + chain
    print("\033[32m" + command + "\033[0m")
    os.system(command)

elif main_option == 3:
    print("\033[1m\033[31mADD RULE\033[0m")
    chain = str(input("\033[33mSelect a chain -> \033[0m"))  # INPUT/FORWARD/OUTPUT/PREROUTING/POSTROUTING/...
    target = str(input("\033[33mSelect a target -> \033[0m"))  # ACCEPT/DROP/REJECT
    print("\033[31m(1) \033[34mProtocol")  # -p
    print("\033[31m(2) \033[34mSource IP")  # -s
    print("\033[31m(3) \033[34mDestination IP")  # -d
    print("\033[31m(4) \033[34mSource Port")  # --sport
    print("\033[31m(5) \033[34mDestination Port")  # --dport
    print("\033[31m(6) \033[34mIn Interface")  # -i
    print("\033[31m(7) \033[34mOut Interface\033[0m")  # -o
    parameter = ""  # -p -s -d -i -o --sport --dport
    parameter_option = int(input("\033[33mSelect a parameter option -> \033[0m"))
    if parameter_option == 1:
        parameter = "-p"
    elif parameter_option == 2:
        parameter = "-s"
    elif parameter_option == 3:
        parameter = "-d"
    elif parameter_option == 4:
        parameter = "--sport"
    elif parameter_option == 5:
        parameter = "--dport"
    elif parameter_option == 6:
        parameter = "-i"
    elif parameter_option == 7:
        parameter = "-o"
    parameter_info = str(input("\033[33mSpecify the protocol/IP/port/interface -> \033[0m"))
    Parameter = parameter + " " + parameter_info
    sub_option = str(input("\033[33mDo you want to add the rule in the last line or in a specify line -> \033[0m"))  # last/specify
    if sub_option == "last":
        command = "iptables -A " + chain + " " + Parameter + " -j " + target
        print("\033[32m" + command + "\033[0m")
        os.system(command)
    elif sub_option == "specify":
        line = int(input("\033[33mEnter the specify line -> \033[0m"))
        command = "iptables -I " + chain + " " + str(line) + " " + Parameter + " -j " + target
        print("\033[32m" + command + "\033[0m")
        os.system(command)

elif main_option == 4:
    print("\033[1m\033[31mDELETE RULE\033[0m")
    chain = str(input("\033[33mSelect a chain -> \033[0m"))  # INPUT/FORWARD/OUTPUT/PREROUTING/POSTROUTING/...
    target = str(input("\033[33mSelect a target -> \033[0m"))  # ACCEPT/DROP/REJECT 
    sub_option = str(input("Do you want to delete the rule in the all lines or in a specify line -> "))  # all/specify
    if sub_option == "all":
        command = "iptables -F " + chain
        print("\033[32m" + command + "\033[0m")
        os.system(command)
    elif sub_option == "specify":
        line = int(input("\033[33mEnter the specify line -> \033[0m"))
        command = "iptables -D " + chain + " " + str(line)
        print("\033[32m" + command + "\033[0m")
        os.system(command)

elif main_option == 5:
    print("\033[1m\033[31mREPLACE RULE\033[0m")
    chain = str(input("\033[33mSelect a chain -> \033[0m"))  # INPUT/FORWARD/OUTPUT/PREROUTING/POSTROUTING/...
    target = str(input("\033[33mSelect a target -> \033[0m"))  # ACCEPT/DROP/REJECT
    print("\033[31m(1) \033[34mProtocol")  # -p
    print("\033[31m(2) \033[34mSource IP")  # -s
    print("\033[31m(3) \033[34mDestination IP")  # -d
    print("\033[31m(4) \033[34mSource Port")  # --sport
    print("\033[31m(5) \033[34mDestination Port")  # --dport
    print("\033[31m(6) \033[34mIn Interface")  # -i
    print("\033[31m(7) \033[34mOut Interface\033[0m")  # -o
    parameter = ""  # -p -s -d -i -o --sport --dport
    parameter_option = int(input("\033[33mSelect a parameter option -> \033[0m"))
    if parameter_option == 1:
        parameter = "-p"
    elif parameter_option == 2:
        parameter = "-s"
    elif parameter_option == 3:
        parameter = "-d"
    elif parameter_option == 4:
        parameter = "--sport"
    elif parameter_option == 5:
        parameter = "--dport"
    elif parameter_option == 6:
        parameter = "-i"
    elif parameter_option == 7:
        parameter = "-o"
    parameter_info = str(input("\033[33mSpecify the protocol/IP/port/interface -> \033[0m"))
    Parameter = parameter + " " + parameter_info
    line = int(input("\033[33mEnter the specify line -> \033[0m"))
    command = "iptables -R " + chain + " " + str(line) + " " + Parameter + " -j " + target
    print("\033[32m" + command + "\033[0m")
    os.system(command)

elif main_option == 6:
    print("\033[1m\033[31mNEW CHAIN\033[0m")
    chain = str(input("\033[33mDefine a new chain -> \033[0m"))
    command = "iptables -N " + chain
    print("\033[32m" + command + "\033[0m")
    os.system(command)

elif main_option == 7:
    print("\033[1m\033[31mDELETE CHAIN\033[0m")
    chain = str(input("\033[33mDefine the chain to delete -> \033[0m"))
    command = "iptables -X " + chain
    print("\033[32m" + command + "\033[0m")
    os.system(command)

elif main_option == 8:
    print("\033[1m\033[31mPERSISTENT\033[0m")
    print("\033[32miptables-save\033[0m")
    os.system("iptables-save")
    print("\033[32miptables-restore\033[0m")
    os.system("iptables-restore")