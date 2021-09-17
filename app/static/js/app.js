$(".submit").on("click", function(e) {
            e.preventDefault();
            search_type = $("#search-type").val();
            search_term = $("#search-term").val();
            $(".book-list").html("");


            var settings = {
                "url": "/search",
                "method": "POST",
                "data": JSON.stringify({
                    "search_type": search_type,
                    "search_term": search_term
                  }),
                };

                $.ajax(settings).done(function (response) {
                console.log(response);
                });
                /*
                $.ajax(settings).done(function(response) {
                        if (response.totalItems != 0) {
                            $.each(response.items, function(index, value) {
                                    $(".book-list").append(' <div class="row">\
                                    <div class = "col-md-3">\
                                        <img src = '+value.volumeInfo.imageLinks.thumbnail+' class = "card-img-top" id="img_'+value.id+'" style="margin:15px;">\
                                    </div>\
                                    <div class = "col-md-9" > \
                                    <div class = "card-body" > \
                                    <h6 class = "card-title" id="title_'+value.id+'">'+ value.volumeInfo.title + '</h6>\
                                    <p class = "card-text" id="author_'+value.id+'" > Authors: '+ value.volumeInfo.authors+'</p>\
                                    <p class="" id="page_'+value.id+'">Pages: '+value.volumeInfo.pageCount+'</p>\
                                    <p class="" id="rating_'+value.id+'">Rating: '+value.volumeInfo.averageRating+'</p>\
                                    <button  class = "btn btn-primary add" id='+value.id+'> Add to my list </buttons> </div > </div > </div > ')
                                    });
                            }
                            else {
                                console.log("Unable to find any books try again!")
                            }
                        });
                }
                else {
                    console.log("Enter search Term!")
                }*/
            });

$(".add").on("click", function(e){
    e.preventDefault();
    book_id = $(this).attr("id");
    var book_info = {
        "book_id" : book_id,
        "img_url" : $("#img_"+book_id),
        "title": $("#title_"+book_id),
        "author": $("#author_"+book_id),
        "pagecount": $("#page_"+book_id),
        "averageRating": $("#rating_"+book_id)
    }

    console.log(book_info);
})