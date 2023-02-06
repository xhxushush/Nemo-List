# fuction to check if small string is
# there in big string
def check(string, sub_str):
    if(string.find(sub_str) == -1):
        print("NAH")
    else:
        print("YESSSSSSS")

#driver code
string = "Nemo is a young clown that likes to pull devious pranks on his family and friends. One time he threw a brick at Patty Pufferfish and knocked him out. As you can see Nemo is a very devious clown fish. And due to his devious pranks he has no friends and is lonely" 

sub_str = "devious"
check(string, sub_str)