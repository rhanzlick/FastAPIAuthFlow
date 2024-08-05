var submit = document.getElementById("submit-btn");
submit.addEventListener('click', function(event) {
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var passwordCheck = document.getElementById("passwordCheck").value;
  
  var validContents = verifyContents(email) && verifyContents(password) && password == passwordCheck;
  // submit.disabled = !validContents

  alert(`email: ${email}\npass1: ${password}\npass2: ${passwordCheck}\n\ncan send: ${validContents}`);
  // submit.innerHTML='clicked'
});
 function verifyContents(inputString){
  return !(inputString === null || inputString === undefined || inputString.trim() === "");
 };
