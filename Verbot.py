const Discord = require('discord.js');

const bot = new Discord.Client();

bot.on('message', (message) => {
	if(message.content == 'Hi') {
		message.reply('Hello budy') 
	}
});

bot.on('message', (message) => {
	if(message.content == 'kasa ho') { message.reply('i am fine')
	}
});

bot.on('message',(message)=> { if (message.content == 'ping') { message.reply('Pong') 
 } 
});

bot.on('message',(message)=> { if (message.content == 'what is the rules')        { message.reply('PLEASE FOLLOLW THE RULES AND MAINTANCE THIS SERVER.                         ================================ (1) No Harrasing bullying and be respectful to other members                         ===============================                (2)No Ear rape when members are talking in voice chat                ===============================                 (3)No discrimniation of relegion , creed , disability                  ===============================    (4)No posting of NSFW content            =============================== (5)Do not Bypass the logos        ===============================     (6)No Abusing Staff members      =============================== (7)Spam is prohibited except in spam channel.                      =============================== (8)Do not use bot command in any other channel except bot command      =============================== (9)Help others                     ===============================       (10)Do not talk in Server Door    ===============================   (11)Dont post links in Community chat and all except Advertising     =============================== (12)Dont be toxic*** https://i.gifer.com/VofE.gif')
 }
});

bot.login('NTk1NjUwNDQ2NjY0Nzk0MTIy.XRuFOg.5XRYZndAtp97eTwZMUcxRcOF9TU');
