let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }

});

$(document).ready(function () {

    $('#orderModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var orderNumber = button.data('order'); 
        var modal = $(this);


        fetch(`/account/order_history/${orderNumber}/`)
            .then(response => response.json())
            .then(data => {
                var orderDetailsHtml = `
                    <p><strong>Order Number:</strong> ${data.order_number}</p>
                    <p><strong>Date:</strong> ${data.date}</p>
                    <p><strong>Total:</strong> $${data.total}</p>
                    <h3>Items:</h3>
                    <ul>
                        ${data.items.map(item => `<li>${item.name} - $${item.price} x ${item.quantity}</li>`).join('')}
                    </ul>
                `;
                modal.find("#order-details-content").html(orderDetailsHtml);
            })
            .catch(error => {
                console.error('Error fetching order details:', error);
                modal.find("#order-details-content").html("<p class='text-danger'>Failed to load order details.</p>");
            });
    });
});