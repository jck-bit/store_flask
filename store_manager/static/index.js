function deleteProduct(id){
    fetch('/delete-Product',{
        method: 'POST',
        body: JSON.stringify({ product_id:id})
    }).then(() =>{
        window.location.reload()
    })
}