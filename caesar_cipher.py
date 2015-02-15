def caesar_encrypt(str, n):
    encrypted_str=""
    for i in str:
        if i.isalpha():
            num=ord(i)+n
            if i.isupper():
                if num>ord("Z"):
                    num-=26
                elif num<ord("A"):
                    num+=26
                encrypted_str+=chr(num)
            elif i.islower():
                if num>ord("z"):
                    num-=26
                elif num<ord("a"):
                    num+=26
                encrypted_str+=chr(num)
        else:
            encrypted_str+=i
    print (encrypted_str)
    return
    
caesar_encrypt("gH", 1)
