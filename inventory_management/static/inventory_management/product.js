var redirect_link

function delete_dialog(product_id) {
    dialog_box = document.getElementById('delete-dialog')
    product_body = document.getElementsByClassName('custom-product-list')[0]
    dialog_box.style.visibility = 'visible'
    product_body.style.opacity = '50%'
    product_body.style.pointerEvents = 'none'
    redirect_link = product_id

}

function delete_redirect(object) {
    location.href = '/delete-' + object + '/' + redirect_link
}

function cancel_delete() {
    dialog_box = document.getElementById('delete-dialog')
    product_body = document.getElementsByClassName('custom-product-list')[0]
    dialog_box.style.visibility = 'hidden'
    product_body.style.opacity = '100%'
    product_body.style.pointerEvents = 'all'
}