<!DOCTYPE html>
<html>
<head>
  <title>Simple Calculator</title>
</head>
<body>
  <h2>Calculator</h2>
  <input type="text" id="result" readonly><br><br>

  <button onclick="append('1')">1</button>
  <button onclick="append('2')">2</button>
  <button onclick="append('3')">3</button>
  <button onclick="append('+')">+</button><br>

  <button onclick="append('4')">4</button>
  <button onclick="append('5')">5</button>
  <button onclick="append('6')">6</button>
  <button onclick="append('-')">-</button><br>

  <button onclick="append('7')">7</button>
  <button onclick="append('8')">8</button>
  <button onclick="append('9')">9</button>
  <button onclick="append('*')">*</button><br>

  <button onclick="append('0')">0</button>
  <button onclick="append('.')">.</button>
  <button onclick="calculate()">=</button>
  <button onclick="append('/')">/</button><br><br>

  <button onclick="clearResult()">C</button>

  <script>
    function append(value) {
      document.getElementById("result").value += value;
    }
    function calculate() {
      try {
        document.getElementById("result").value =
          eval(document.getElementById("result").value);
      } catch {
        document.getElementById("result").value = "Error";
      }
    }
    function clearResult() {
      document.getElementById("result").value = "";
    }
  </script>
</body>
</html>


click win+R 
     	Write cmd
     	Write ipconfig
    	 Copy the ip4 address

http://[Your-PC-IP]:[Port]/Cal.html

-------------------------------------------

npx create-react-app myapp
cd myapp

npm install firebase-tools

firebase login
firebase init

npm run build
firebase deploy

------------------------------------------

sudo yum update -y
sudo yum install httpd -y

sudo systemctl start httpd
sudo systemctl enable httpd

cd /var/www/html
sudo nano index.html

ctrl+o -> Enter to save -> ctrl+x to exit

open in different browser id same browswer dont work
