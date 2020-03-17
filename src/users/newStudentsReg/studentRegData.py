def getPasswords(filePath):
    users = {}
    try:
        with open(filePath,'r') as fp:
            for user in fp:
                idno,passwd = user.split(':')   # idno, passwd in str datatype
                users[idno] = passwd[:-1]
    except Exception as e:
        print(e)
    # print(users)
    return users

def getNewStudentData():
    import os

    base_dir = os.getcwd()

    pswd_file_path = os.path.join(base_dir, 'users', 'newStudentsReg', 'passwords.txt')
    passwords = getPasswords(pswd_file_path)

    data_path = os.path.join(base_dir,'users','newStudentsReg','newStudentsData')
    user_date = {}

    for root, dirs, files in os.walk(data_path):
        for file in files:
            filePath = os.path.join(data_path, file)
            with open(filePath,'r') as fp:
                for line in fp:
                    idno=line[:-1]
                    user_date[idno]=passwords[idno]
                    
    return user_date
