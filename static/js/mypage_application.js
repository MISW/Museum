$(function(){

    $("#gameImageInput").on('change',function(e){
        if(!e.target.files[0]){
            $("#gameImage").attr('src',"");
            return;
        }

        var reader = new FileReader();
        reader.onload = function (e) {
            $("#gameImage").attr('src', e.target.result);
            $("#gameImage").attr('width', 256+"px");
        }
        reader.readAsDataURL(e.target.files[0]);
    });


    //共同作成者
    $('input[name="developer"]').on('change',function(){
        var co_developers="";
        $('input[name="developer"]:checked').each(function(){
                co_developers+=$(this).next("label").text()+",  ";
        });
        $("#co_createdBy").text(co_developers);
    });


    //linkの必要不必要管理  見たらわかるようにele→label→div↓input という厳密な順番でないと使えない
    function link_required_prop(ele){
        ele.on('change',function(){
            if($(this).prop('checked')){
                console.log(0);
                $(this).next('label').next('div').children('input').prop('required',true);
            }else{
                console.log(1);
                $(this).next('label').next('div').children('input').prop('required',false);
                $(this).next('label').next('div').children('input').val("");//入力を消す
            }
        });
    }
    link_required_prop($("#check0"));
    link_required_prop($("#check1"));
    link_required_prop($("#check2"));
    link_required_prop($("#check3"));
    link_required_prop($("#check4"));





    //ページ移動警告
    $("input").change(function() {
        $(window).on('beforeunload', function(e) {
            return '入力済みデータが失われます。このまま移動しますか？\n申請する場合は「このまま移動する」を押してください。';
        });
    });
    $("button[type=submit]").click(function() {
        $(window).off('beforeunload');
    });




    //formの中身をalertで表示
    $('form').submit(
        //$('#submit').click(
        function(){
            var message="";
            message+="ゲームタイトル: "+$("#gameTitle").val();
            message+="\nゲームの説明: "+$("#introduction").val();
            message+="\n作成者: "+"your name";
            message+="\n作成者（申請者以外）: ";
            $('input[name="developer"]:checked').each(function(){
                message+=$(this).next("label").text()+",  ";
            });

            message+="\nゲームカテゴリ： "+ $('#gameCategory option:selected').text();

            //message+="\nイメージ画像: "+$("#gameImage").val();

            message+="\nダウンロードリンク: ";
            if($("#check0:checked").val())message+="\nブラウザ: "+$("#link0").children("input").val();
            if($("#check1:checked").val())message+="\nWindows: "+$("#link1").children("input").val();
            if($("#check2:checked").val())message+="\nMac: "+$("#link2").children("input").val();
            if($("#check3:checked").val())message+="\nAndrois: "+$("#link3").children("input").val();
            if($("#check4:checked").val())message+="\niOS: "+$("#link4").children("input").val();


            message+="\n\nで申請します。";
            alert(message);

        }
    );    
    

});