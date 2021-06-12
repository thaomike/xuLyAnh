var express = require('express');
var router = express.Router();
var multer = require('multer');
// var upload = multer({ dest: 'uploads/' });
var spawn = require('child_process').spawn;
var path = require("path")

let diskStorage = multer.diskStorage({
  destination: (req, file, callback) => {
    // Định nghĩa nơi file upload sẽ được lưu lại
    callback(null, "uploads/");
    // callback(null, "/../public/images")
  },
  filename: (req, file, callback) => {
    // ở đây các bạn có thể làm bất kỳ điều gì với cái file nhé.
    // Mình ví dụ chỉ cho phép tải lên các loại ảnh png & jpg
    let math = ["image/png", "image/jpeg"];
    if (math.indexOf(file.mimetype) === -1) {
      let errorMess = `The file <strong>${file.originalname}</strong> is invalid. Only allowed to upload image jpeg or png.`;
      return callback(errorMess, null);
    }
    // Tên của file thì mình nối thêm một cái nhãn thời gian để đảm bảo không bị trùng.
    let filename = `${Date.now()}-${file.originalname}`;
    callback(null, filename);
  }
});

let uploadFile = multer({ storage: diskStorage }).single('fname');


router.get('/', function image(req, res) {

  //E.g : http://localhost:3000/?firstname=van&lastname=nghia

    res.render('index')
})

router.post('/', function (req, res) {
  uploadFile(req, res, err => {
    console.log(req.body)
    var control = 0;
    python = [
      './process.py',
        // req.file.path,
        // 1
        // req.params.action,
    ]
    if(req.body.btn) {
      python = [...python, req.file.path, 1];
      control = 1;
    }
    else if(req.body.hsv && req.body.hsv != '') {
      pathCat = 'uploads\\' + req.body.var;
      python = [...python, pathCat, 2, req.body.H, req.body.S, req.body.V];
      control = 2;
    }
    else if(req.body.xoay != '') {
      pathCat = 'uploads\\' + req.body.var;
      python = [...python,pathCat, 3, req.body.xoay];
      control = 3;
    }
    
    if (err) {
      return res.send(`Error when trying to upload: ${err}`);
    }
    else {
      var process = spawn('python', python);
      process.stdout.on('data', function (data) {
        console.log(data.toString())
        if(control == 1){
          var file = `${req.file.filename}`;
          res.render('index', 
          {
            data: true,
            path: file,
            xam: 'xam'+file,
            bien: 'bien' + file,
            cat: 'cat'+file,
            detect: "detect" + file,
          });
        }
        else if(control == 2) {
          file = req.body.var
          req.body.xoayPath != 'undefined' ?
          res.render('index', 
          {
            data: true,
            path: file,
            xam: 'xam'+file,
            bien: 'bien' + file,
            cat: 'cat'+file,
            detect: "detect" + file,
            hsv: "hsv" + file,
            xoay: 'xoay' + file
          })
           :
          res.render('index', 
          {
            data: true,
            path: file,
            xam: 'xam'+file,
            bien: 'bien' + file,
            cat: 'cat'+file,
            detect: "detect" + file,
            hsv: "hsv" + file,
          });
        }
        else if(control == 3) {
          file = req.body.var
          req.body.hsvPath != 'undefined' ?
          res.render('index', 
          {
            data: true,
            path: file,
            xam: 'xam'+file,
            bien: 'bien' + file,
            cat: 'cat'+file,
            detect: "detect" + file,
            hsv: "hsv" + file,
            xoay: 'xoay' +file
          }) :
          res.render('index',{
            data: true,
            path: file,
            xam: 'xam'+file,
            bien: 'bien' + file,
            cat: 'cat'+file,
            detect: "detect" + file,
            xoay: 'xoay' +file
          }) ;
        }
      });
    }
  })

});

module.exports = router;
