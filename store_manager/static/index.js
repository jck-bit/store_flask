function deleteProduct(id){
    fetch('/delete-product',{
        method: 'POST',
        body: JSON.stringify({id}),
    }).then(() =>{
        window.location.reload();
    })
}
