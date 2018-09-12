function required()
{
    var empty1 = document.form1.username.value;
    var empty2 = document.form1.password.value;

    if (empty1 === "" || empty2 === "")
        {
        alert("Please input a Value");
        return false;
        }
    else
        {
        alert('Code has accepted : you can try another');
        return true;
        }
}