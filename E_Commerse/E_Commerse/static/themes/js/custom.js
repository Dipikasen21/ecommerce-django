// $(document).ready(function () {
//     console.log("Hello ================= World!!")
//     $('.increment-btn').click(function (e) {
//         e.preventDefault()
//         console.log("Hello")
//         var inc_value = $(this).find('.qty-input').val()
//         var value = parseInt(inc_value, 10)
//         value = isNaN(value) ? 0 : value;
//         console.log("Value is:", $(this).find('.qty-input').val(value))
//         if (value<10) {
//             value++
            
//             $(this).find('.qty-input').val(value);
//         }
       
//     })
//     $('.decrement-btn').click(function (e) {
//         e.preventDefault()
       
//         var dec_value = $(this).find('.qty-input').val()
//         var value = parseInt(dec_value, 10)

//         value = isNaN(value) ? 0 : value;
//         console.log("Value is:", $(this).find('.qty-input').val(value))
//         if (value>1) {
//             value--
            
//             $(this).find('.qty-input').val(value);
//         }
        
//     })
// })

function increment(){
    var value = document.getElementsByClassName('qty-input').value()
    console.log(value)
}
