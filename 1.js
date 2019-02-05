//此js为单线程huya弹幕爬虫，根据huya-danmu test文件改写

const huya_danmu = require('huya-danmu')
const sd = require('silly-datetime')
const mysql      = require('mysql')

//const client2 = new huya_danmu(roomid)
const roomid = '11342412'
const client = new huya_danmu(roomid)
const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '123456',
  database : 'huya'
});
 
//connection.connect();

function danmu (connection,list1){
	
	var  addSql = 'INSERT INTO danmu(ID,rid,name,content,room,time) VALUES(0,?,?,?,?,?)';
	var  addSqlParams = list1;
	//增
	connection.query(addSql,addSqlParams,function (err, result) {

        if(err){
         	console.log('[INSERT ERROR] - ','弹幕无法识别');
        	return "cuocuocuo";
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


    client.start()

    client.on('connect', () => {
        console.log(`已连接huya ${roomid}房间弹幕~`)
                                })

    client.on('message', msg => {
        switch (msg.type) {
            case 'chat':
                var time=sd.format(new Date(), 'YYYY-MM-DD HH:mm:ss');
                console.log(`[${msg.from.name}]:${msg.content}`)
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

