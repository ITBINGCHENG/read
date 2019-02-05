//2 3 js为多线程虎牙弹幕爬虫，3为多线程执行文件。

const huya_danmu = require('huya-danmu')
const sd = require('silly-datetime')
const mysql      = require('mysql')


//const client2 = new huya_danmu(roomid)
const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '123456',
  database : 'huya'
	});

// i = process.argv[2]//多线程传参数？
const roomid = process.argv[3]

 
//connection.connect();

function danmu (connection,list1){
	
	var  addSql = 'INSERT INTO danmu2019年1月29日(ID,rid,name,content,room,time) VALUES(0,?,?,?,?,?)';
	var  addSqlParams = list1;
	//增
	connection.query(addSql,addSqlParams,function (err, result) {

        if(err){
         	console.log('[INSERT ERROR] - ',`弹幕无法识别${addSqlParams[2]}`);
        	return;
        }        
 
		});
 
	}
function gift (connection,list1){
	
	var  addSql = 'INSERT INTO gift(ID,rid,name,gift,room) VALUES(0,?,?,?,?)';
	var  addSqlParams = list1;
	//增
	connection.query(addSql,addSqlParams,function (err, result) {

        if(err){
         	console.log('[INSERT ERROR] - ','礼物无法识别');
        	return;
        }        
 
		});
 
	}


//var roomid = roomids[i]
var client = new huya_danmu(roomid)

client.start()

client.on('connect', () => {
    console.log(`已连接huya ${roomid}房间弹幕~`)
							})

client.on('message', msg => {
    switch (msg.type) {
        case 'chat':

			var time=sd.format(new Date(), 'YYYY-MM-DD HH:mm:ss');
            //console.log(`${roomid}:[${msg.from.name}]:${msg.content}`)
            var list1 = [`${msg.from.rid}`,`${msg.from.name}`,`${msg.content}`,`${roomid}`,`${time}`]
            danmu(connection,list1);

            break
        case 'gift':
        	var list1 = [`${msg.from.rid}`,`${msg.from.name}`,`${msg.count}个${msg.name}`,`${roomid}`]
            gift(connection,list1);
            //console.log(`[${msg.from.name}]->赠送${msg.count}个${msg.name}`)
            break
        case 'online':
            //console.log(`[当前人气]:${msg.count}`)
            break
    				}
							})

client.on('error', e => {
    console.log(e)

						})

client.on('close', () => {
    console.log('close')
    client.start()
					})