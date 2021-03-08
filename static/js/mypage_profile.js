$(function(){

    //画像変更
    const input=$("#id_image");
    const output=$("#id_image_output");
    input.on('change',function(e){
        if(!e.target.files[0]){
            output.attr('src',"");
            return;
        }

        var reader = new FileReader();
        reader.onload = function (e) {
            output.attr('src', e.target.result);
            output.attr('width', 200);
            output.attr('height', 200);
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
            var message="";
            message+="代:　　　　　"+$('input[name="generation"]').val();
            message+="\n研究会:　　　";
            $(".checkbox").each(function(){
                if($(this).find('input[name="associations"]').prop("checked")==true){
                    message+=$(this).find('.association_name').text()+", ";
                }
            });
            message+="\nひとこと:　\n「"+$('textarea[name="description"]').text()+"」";
            message+="\nで登録します。";
            alert( message );
        } 
    );
assosiations

})