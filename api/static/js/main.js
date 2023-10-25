let form = document.forms.dateform;
const buttons = document.querySelectorAll(".button")
const cards = document.querySelectorAll(".review")

$("#date").on('change', function () {
    const mydate = new Date($(this).val());
    const date_parse = `${mydate.getDate()}.${mydate.getMonth()+1}.${mydate.getFullYear()}`;
    //const token = document.getElementsByName('csrfmiddlewaretoken')[0].value
    $.ajax({
        type: "GET",
        url: `${date_parse}`,
        //data: {
        //    "date_parser": String(mydate),
            //"csrfmiddlewaretoken": token
        //},
        success: function () {
            console.log(arguments[0].create_at, arguments[0].raiting, arguments[0].count_comments);
            document.getElementById("create_at_date").textContent = arguments[0].create_at;
            document.getElementById("raiting_date").textContent = arguments[0].raiting;
            document.getElementById("count_comments_date").textContent = arguments[0].count_comments;
            document.getElementById("recommend_date").textContent = arguments[0].recommend;
        }
    })
})



function filter(status, items) {
    items.forEach((item) => {

        const allChildren = item.children
        const bool = !allChildren[1].classList.contains(status)
        const isShowAll = status === 'all'

        if (bool && !isShowAll) {
            item.classList.add('hide')
        }
        else {
            item.classList.remove('hide')
        }
    })
}

buttons.forEach((button) => {
    button.addEventListener('click', () => {
        const status = button.dataset.filter
        filter(status, cards)
    });
})