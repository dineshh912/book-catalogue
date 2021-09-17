$(".add").on("click", function(e) {
    e.preventDefault();
    book_id = $(this).attr("id");
    img_url = $("#img_" + book_id).attr('src');
    title = $("#title_" + book_id).html();
    author = $("#author_" + book_id).html();
    pagecount = $("#page_" + book_id).html();
    averageRating = $("#rating_" + book_id).html();
    var settings = {
        "url": "/add",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
        },
        "data": JSON.stringify({
            "book_id": book_id,
            "info": {
                "img_url": img_url,
                "title": title,
                "author": author,
                "pagecount": pagecount,
                "averageRating": averageRating
            }
        }),
    };

    $.ajax(settings).done(function(response) {
        alert("Successful Message");
        location.reload();
    });
});