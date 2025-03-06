$(document).ready(function () {
    $("#search").on("input", function () {
        let search_query = $(this).val();

        $.ajax({
            url: "/orders/",
            method: "GET",
            data: {
                "q": search_query
            },
            success: function (orders) {
                $(".tbody-orders").empty();

                for (let order of orders) {
                    let order_html = `<tr onclick=location.href="${order.get_absolute_update_url}";>
                        <td>${order.id}</td>
                        <td>${order.table_number}</td>
                        <td>
                            ${order.dishes.join(", ")}
                        </td>
                        <td>${order.total_price} ₽</td>
                        <td class="status-${order.status.toLowerCase()}">
                            ${order.status_display}
                        </td>
                    </tr>`;

                    $(".tbody-orders").append(order_html);
                }
            }
        });
    });
});
