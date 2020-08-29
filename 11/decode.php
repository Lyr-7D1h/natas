<?php
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_decrypt($input) {
    $result = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D");
    $key = "";

    // Iterate through each character
    for($i=0;$i<strlen($input);$i++) {
        $key .= $input[$i] ^ $result[$i % strlen($result)];
    }

    return $key;
}

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

// echo xor_decrypt(json_encode($defaultdata));
echo base64_encode(xor_encrypt(json_encode(array( "showpassword" => "yes", "bgcolor" => "#ffffff"))))
// echo base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D");
// echo xor_encrypt("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D");
?>
