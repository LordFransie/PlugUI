// vim: sw=4:ts=4:nu:nospell:fdc=4
/**
 * An Application
 *
 * @author    Ing. Jozef Sakáloš
 * @copyright (c) 2008, by Ing. Jozef Sakáloš
 * @date      2. April 2008
 * @version   $Id: filetree.js 113 2009-02-02 02:27:23Z jozo $
 *
 * @license application.js is licensed under the terms of the Open Source
 * LGPL 3.0 license. Commercial use is permitted to the extent that the 
 * code/component(s) do NOT become part of another Open Source or Commercially
 * licensed development library or toolkit without explicit permission.
 * 
 * License details: http://www.gnu.org/licenses/lgpl.html
 */
 
/*global Ext, WebPage, window */

Ext.BLANK_IMAGE_URL = '/static/ext-2.3.0/resources/images/default/s.gif';
Ext.state.Manager.setProvider(new Ext.state.CookieProvider);

Ext.onReady(function() {
    Ext.QuickTips.init();
    Ext.form.Field.prototype.msgTarget = 'side';
    document.cookie = 'locale=en_US';


	// window with uploadpanel
//    	var win = new Ext.Window({
//         width:180,
//	minWidth:165,
//	id:'winid',
//	height:220,
//	minHeight:200,
//	stateful:false,
//        layout:'fit',
//        border:false,
//        closable:false,
//        title:'UploadPanel',
//	iconCls:'icon-upload',
//	items:[{
//			 xtype:'uploadpanel',
//			 buttonsAt:'tbar',
//			 id:'uppanel',
//			 url:'filetree.php',
//			 path:'root',
//			 maxFileSize:1048576,
//			 enableProgress:false,
//			 singleUpload:true
//		}]
//   });


//    win.show.defer(500, win);

	var treepanel = new Ext.ux.FileTreePanel({
		height:400,
		autoWidth:true,
		id:'ftp',
		title:'File Browser',
		renderTo:'treepanel',
		rootPath:'',
		topMenu:false,
		autoScroll:true,
		enableProgress:false,
//		baseParams:{additional:'haha'},
//		singleUpload:true
	});

});
