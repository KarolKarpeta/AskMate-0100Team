function required()
{
    var empty1 = document.form1.username.value;
    var empty2 = document.form1.password.value;

    if (empty1 === "" || empty2 === "")
        {
        alert("PLEASE INPUT A VALUE");
        return false;
        }
    else
        {
        alert('USER REGISTERED CORRECTLY');
        return true;
        }
}