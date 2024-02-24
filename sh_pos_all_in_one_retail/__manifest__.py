# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
{
    "name": "Point of Sale Retail Shop| POS Retail Shop| All In One POS Retail",         
    "author": "Softhealer Technologies",     
    "website": "https://www.softhealer.com",     
    "support": "support@softhealer.com",     
    "category": "Point of Sale",   
    "version": "0.0.1",       
    "summary": """Retail Point Of Sale Solution Retail POS cash in cash out own customer discount mass update product tags own product template auto validate pos quick print receipt import pos secondary product suggestion pos access right pos auto lock cancel whatsapp return exchange pos all feature Restaurant & Shop Retail All In One POS Enterprise POS Community All In One POS all in one features pos Reorder pos Reprint pos Coupon Discount pos Order Return pos order all pos all features pos discount pos order list print pos receipt pos item count retail pos retail import sale from pos create quote from pos odoo All in one pos Reprint pos Return POS Stock pos gift import sale from pos multi currency payment pos pay later pos internal transfer pos disable payment pos product template pos product operation pos loyalty rewards all pos reports pos stock pos retail pos label pos cash control pos cash in out pos cash out pos logo pos receipt all pos in one all pos in one retail  odoo All in One Point of Sale Point of Sale Features POS Features Product Multi barcode for POS POS Multi barcode Discount in POS Customer DIscount Point of sale POS Category Slider Point of Sale category slider Import POS Order from Excel Import POS Order from CSV Import Multiple POS Orders Import Multiple POS Orders from Excel Import Multiple POS Orders from CSV POS Realtime Quantity Update POS Realtime Qty Update POS Realtime Stock Update Realtime Stock Update POS Disable Button Option POS Disable Button Feature Disable Button POS POS Hide Button Disable Button Access Create PO from POS Create Purchase Order from POS Create PO from Point of Sale Create Purchase Order from Point of Sale Generate Purchase Order from POS Request for Quotation from POS Request for Quotation from Point of Sale RFQ from POS RFQ from Point of Sale Create Purchase Order POS Product Variants Popup POS all in one features pos Reorder pos Reprint pos Coupon Discount pos Order Return POS Stock pos gift pos order all pos all features pos discount pos order list print pos receipt pos item count retail pos retail import sale from pos create quote from pos Point of Sale Product Variants Popup POS Product Multi Variants Select Product Variants Product Variant Suggestion POS Orderlist Filter Point of Sale Orderlist Filter Orderlist Filter in POS Order list Filter Point of Sale Order list Filter Order list Filter In POS SO from POS Sale order from POS Sale order from Point of Sale SO from Point of Sale Quotation form POS Quotation form Point of Sale Generate Sale Order from POS Generate Quotation from POS POS Product Suggestion POS Related Products Point of Sale Product Suggestion Pos Recommended products  Dsiplay Related Product  POS Product Weight and Volume POS Product Weight  POS Product Volume POS Product Volume information POS Product Weight Information POS Product Weight Details POS Product Volume Details Point Of Sale Secondary Unit Of Measure POS multiple UOM POS multiple Unit of Measure Product Unit of Measure Multiple Unit of Measure POS Portal Portal POS Point of Sale Portal Portal Point of Sale POS Product Bundle Sale Combo Combo of Product Bundle of products Pack of Products Combine two or more Products in POS Access Rights in POS POS Access Rights Disable Discount Button  Disable Price Button  Disable Plus minus Button  Disable Payment Button  Restrict Numpad Auto Lock POS POS Screen Auto Lock Auto Lock Screen POS Session Lock Auto Lock POS Bag Charges POS Carry Bag Charges POS Carry Bag Option Bag Charges Carry Bag Charges Carry Bag Option POS Bag Size Option Add Bag Charges Add Carry Bag Charges Cancel POS Orders Cancel Point of Sale Order POS Order Cancellation Cancel Order Delet POS Order POS Chatter Add Chatter in POS Add Chatter in Point of Sale Point of Sale Chatter Chatter History POS Chatbot Point of Sale Chatbot POS Item Counter Item Counter Point of Sale Product Counter POS Product Couter POS Item Calculator POS Product Count POS Default Customer Point of Sale Default Customer POS Default Invoice Point of Sale Default Invoice Point of Sale Default Customer Invoice POS Default Customer Invoice POS Bydefault Customer POS Bydefault Invoice POS Login POS Direct Login POS Signin POS Direct Sign in POS Keyboard Shortcut Custom Keyboard POS Custom Keyboard POS Shortcut Key Access POS Shortcut POS Pricelist POS Logo Point of Sale Logo POS Custom Logo POS Notes POS Line Notes Point of Sale Order Line Notes Point of Sale Order List POS Remove Cart Item Point of Sale Remove Cart Item Point of Sale Cart Item Remove POS Item Remove POS Clear Cart POS Delet Cart Item POS Cart Clear Remove Cart Item POS Rounding POS Rounding Amount POS Rounding Enable Point of Sale Rounding Cash Rounding Rounding Payment Rounding Rounding Off POS Customisation POS Customization Point of Sale Customization POS Stock Display POS Stock Quantity  POS on Hand Quantity POS Inventory Stock Quantity POS Forecasted Quantity POS Incoming Quanity POS Whatsapp Integration Whatsapp Inetegration Point of Sale Whatsapp Integration POS Own Customer POS Specific customer Salesperson specific customer POS Special Customer User Own Customer POS User Own Customer POS User wise Customer POS Own Product POS Specific Product POS User Specific Product POS User own Product POS Saleperson Specific Product POS Product Tags Point of Sale Product Tags POS Product Search by Tags POS Tags Search Product Tags Search Auto Validate Point of Sale POS Auto Validate  Auto Validate  Auto POS Session Auto Validate POS Session POS Order Product Template Product Custom Template POS Product Template Build POS Product Multiple Template POS Product Variants POS Product Multiple Variants Merge Categories POS Categories Merge POS Merge Categories Point of Sale Discount POS Custom Discount POS Sale Line Discount POS Discount Odoo POS Receipt With Discount Employee Discount POS Employee Discount Product Code POS Product Code MAnage Product Code Product Quantity Pack Product Pack Product Package Product Bundle Product Combo POS Product Pack Customize Product Pack Customize Product Bundle POS Section Point of Sale Label POS Order Label POS Category POint of Sale Cart Line Label POS Cart Line LAbel POS exchange POS Return and exchange POS Order Exchange Point of Sale Order Exchange Point of Sale Order Return Manage Return Manage Exchange POS Product Return POS Product Exchange POS Product Return Odoo POS Refund POS All in one pos all in one pos point of sale all in one point of sale Odoo What Is a Retail POS Solution What Is a Retail Point Of Sale Solution Retail POS System Retail Point Of Sale System Retail Point of Sale Software Retail POS Software Top Retail POS Systems Top Retail Point Of Sale Systems Best Retail POS Best Point Of Sale Retail Best Retail Point Of Sale POS All In One Point of sales All In One POS Responsive POS Order History POS Order List POS Bundle POS Signature POS Keyboard Shortcut POS Direct Login POS Toppings POS Orders With Type POS Order Type""",          
    "description": """ This is the fully retail solution for any kind of retail shop or bussiness.  """,
    "depends": ["point_of_sale"],
    "data": [
        'data/sh_pos_theme_responsive/data/pos_theme_settings_data.xml',
        
        'sh_pos_theme_responsive/security/ir.model.access.csv',
        'sh_pos_theme_responsive/views/sh_pos_theme_settings_views.xml',
        'data/order_label.xml',
        'views/pos_order.xml',
        'views/res_config_settings.xml',
        'data/sh_pos_keayboard_shortcut/data/sh_keyboard_key_data.xml',
        'security/ir.model.access.csv',

        # varaint
        'sh_pos_product_variant/views/product_template.xml',

        # product suggtion
        'pos_product_suggestion/views/product_view.xml',

        'sh_pos_cash_in_out/views/cash_in_out_menu.xml',

        'sh_pos_product_toppings/views/pos_category_views.xml',
        'sh_pos_product_toppings/views/product_product_views.xml',
        'sh_pos_product_toppings/views/sh_product_toppings.xml',
        'sh_pos_product_toppings/views/sh_topping_group.xml',

        'sh_base_order_type/security/ir.model.access.csv',
        'sh_pos_order_type/views/sh_order_type_views.xml',
        'sh_pos_order_type/views/pos_order_views.xml',

        'sh_product_multi_barcode/security/ir.model.access.csv',
        'sh_product_multi_barcode/views/product_product_views.xml',
        'sh_product_multi_barcode/views/product_template_views.xml',
        'sh_product_multi_barcode/views/res_config_settings.xml',



    ],
    'assets': {'point_of_sale._assets_pos': [
            # theme
            '/sh_pos_all_in_one_retail/static/sh_pos_theme_responsive/static/src/overrides/pos_theme_variables.scss',
            'sh_pos_all_in_one_retail/static/sh_pos_theme_responsive/static/src/scss/mixin.scss',
            'sh_pos_all_in_one_retail/static/sh_pos_theme_responsive/static/lib/owl.carousel.js',
            'sh_pos_all_in_one_retail/static/sh_pos_theme_responsive/static/lib/owl.carousel.css',
            'sh_pos_all_in_one_retail/static/sh_pos_theme_responsive/static/lib/owl.theme.default.min.css',
            'sh_pos_all_in_one_retail/static/sh_pos_theme_responsive/static/src/overrides/**/*',
            'sh_pos_all_in_one_retail/static/sh_pos_theme_responsive/static/src/scss/**/*',

            # pos counter
            'sh_pos_all_in_one_retail/static/sh_pos_counter/**/*',

            # create sale order from pos
            'sh_pos_all_in_one_retail/static/sh_pos_create_so/static/src/**/*',

            # Create purchase order from pos
            'sh_pos_all_in_one_retail/static/sh_pos_create_po/static/src/**/*',

            # pos order label
            'sh_pos_all_in_one_retail/static/sh_pos_order_label/static/src/**/*',

            # order list
            'sh_pos_all_in_one_retail/static/sh_pos_order_list/static/**/*',

            # Global pos models
            'sh_pos_all_in_one_retail/static/global_models/static/src/override/pos_store.js',
            
            # receipt extend
            'sh_pos_all_in_one_retail/static/sh_pos_receipt_extend/static/src/**/*',

            # variant merge
            'sh_pos_all_in_one_retail/static/sh_pos_product_variant/static/src/**/*',

            # Wh stock
            'sh_pos_all_in_one_retail/static/sh_pos_wh_stock/static/src/app/**/*',
            'sh_pos_all_in_one_retail/static/sh_pos_wh_stock/static/src/scss/**/*',

            # remove cart item
            'sh_pos_all_in_one_retail/static/sh_pos_remove_cart_item/static/src/**/*',

            # keayboard
            'sh_pos_all_in_one_retail/static/sh_pos_keyboard_shortcut/static/src/**/*',  

            # discount
            'sh_pos_all_in_one_retail/static/sh_pos_order_discount/static/src/**/*',

            # suggestion
            'sh_pos_all_in_one_retail/static/pos_product_suggestion/static/src/**/*',

            'sh_pos_all_in_one_retail/static/sh_pos_product_code/static/src/**/*',

            'sh_pos_all_in_one_retail/static/sh_pos_cash_in_out/static/src/**/*',

            'sh_pos_all_in_one_retail/static/sh_pos_product_toppings/static/src/app/**/*',
            'sh_pos_all_in_one_retail/static/sh_pos_product_toppings/static/src/overrides/components/product_screen/product_screen.js',
            'sh_pos_all_in_one_retail/static/sh_pos_product_toppings/static/src/overrides/models/pos_store.js',
            'sh_pos_all_in_one_retail/static/sh_pos_product_toppings/static/src/overrides/models/models.js',
            'sh_pos_all_in_one_retail/static/sh_pos_product_toppings/static/src/overrides/orderline/orderline.js',
            'sh_pos_all_in_one_retail/static/sh_pos_product_toppings/static/src/overrides/orderline/orderline.scss',
            'sh_pos_all_in_one_retail/static/sh_pos_product_toppings/static/src/overrides/orderline/orderline.xml',

            'sh_pos_all_in_one_retail/static/sh_pos_order_type/static/**/*',
            'sh_pos_all_in_one_retail/static/sh_pos_multi_barcode/static/src/overrides/**/*'
        ]
    },
    "images": [
        'static/description/splash-screen.gif',
        'static/description/splash-screen_screenshot.gif'

    ],
    "application": True,
    "auto_install": False,
    "license": "OPL-1",
    "price": 210,
    "installable": True,
}
