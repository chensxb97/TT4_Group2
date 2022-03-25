async function submitUserInfo(){
    const response = await fetch('https://reqres.in/api/products/3')
    const data = await response.json();
    alert(data);
}