<?php
/**
 * Created by PhpStorm.
 * User: didi
 * Date: 2019/1/19
 * Time: 2:49 PM
 */

class unauthtest extends MY_Controller {

    public function __construct()
    {
        parent::__construct();
    }



    public function JsonOne() {
        /*
        $data = array('one'=>array(1,'admin','password','92dba1557946c160e4c49792f66bc4dd'),'two'=>array(2,'body','body','d5e12f8b7e120e20a77010397a6a7f04'));
        $datawrite = $data[array_rand($data,1)];
        $result = array('id'=>$datawrite[0],'username'=>$datawrite[1],'password'=>$datawrite[2],'hash'=>$datawrite[3]);
        */
        $result = array('id'=>$this->idrand(''),'username'=>$this->stringrand(16),'password'=>$this->stringrand(32),'hash'=>$this->hash());
        $this->renderJson($result,'sucess');
    }

    public function JsonTwo() {
        $result = array();
        $auth = array('id'=>$this->idrand(''),'username'=>$this->stringrand(16),'password'=>$this->stringrand(32),'hash'=>$this->hash());
        $info = array('phone'=>$this->idrand(11),'company_id'=>$this->idrand(16),'address'=>$this->stringrand(16));
        $result[] = $auth;
        $result[] = $info;
        $this->renderJson($result,'suceess');
    }

    public function Error() {
        $this->renderJson('you data is wrong please input the right data','error');
    }

    private function idrand($len){
        $len = $len ? $len:rand(1,8);
        $data = '';
        for($i=0;$i<$len;$i++) {
            $data .= rand(0,9);
        }
        return $data;
    }

    private function stringrand($len) {
        $char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $data = '';
        for ($i=0;$i<$len;$i++) {
            $data .= substr($char,rand(0,strlen($char)-1),1);

        }
        //var_dump(strlen($data));
        return $data;
    }

    private function hash() {
        return md5(uniqid(microtime(true),true));
    }
}
