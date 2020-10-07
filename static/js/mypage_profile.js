  //画像変更
  $("#profileImageInput").on('change',function(e){
    if(!e.target.files[0]){
        $("#profileImage").attr('src',"");
        return;
    }

    var reader = new FileReader();
    reader.onload = function (e) {
        $("#profileImage").attr('src', e.target.result);
        $("#profileImage").attr('width', 200);
        $("#profileImage").attr('height', 200);
    }
    reader.readAsDataURL(e.target.files[0]);
});

//変更ボタン表示
/*$("#changeButton").hide();
$("input").on('click',function() {
    $("#changeButton").show('slow');
});
$("textarea").on('click',function() {
    $("#changeButton").show('slow');
});*/


//ページ移動警告
/*
$("input").change(function() {
    $("#changeButton").show("slow");
    $(window).on('beforeunload', function(e) {
        return '入力済みデータが失われます。このまま移動しますか？\n申請する場合は「このまま移動する」を押してください。';
    });
});
$("input[type=submit]").click(function() {
    $(window).off('beforeunload');
});*/



$('form').submit(
    function(){
        alert("「ひとこと」を「"+$('#shortCommentInput').val()+"」、\n「代」を"+$('#generationInput').val()+"に変更します。");
    } 

);