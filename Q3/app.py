from flask import Flask, request

app = Flask(__name__)

def check_palindrome(num):
    temp=num
    rev=0
    
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10

    if(temp==rev):
        return True
    else:
        return False

@app.route("/", methods=["GET"])
def home():
    num = request.args.get("num", default=100, type=int)
    res = check_palindrome(num)

    if res:
        return f"<h1>{num} is a palindrome number</h1>"
    else:
        return f"<h1>{num} isn't a palindrome number</h1>"

if __name__ == "__main__":
    app.run(debug=True)