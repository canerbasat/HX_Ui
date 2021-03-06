HX Case
=====================


HX Case
-----------------------------------------------------------
tags:stepbyStep
* "btn_MainPage_SignIn" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=authentication&back=my-account" olması beklenir
* "tb_SignInPage_EmailAdress" alanına rastgele "email" yazilir
* "btn_SignInPage_CreateAnAccount" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation" olması beklenir
* "btn_CreateAnAccount_GenderMr" elementine tıklanır
* "tb_CreateAnAccount_FirstName" elementine "Caner" değeri yazilir
* "tb_CreateAnAccount_LastName" elementine "Basat" değeri yazilir
* "tb_CreateAnAccount_Password" elementine "123123Test" değeri yazilir
* "slt_CreateAnAccount_DateOfBirth_Day" listesinden "12" degeri secilir
* "slt_CreateAnAccount_DateOfBirth_Month" listesinden "11" degeri secilir
* "slt_CreateAnAccount_DateOfBirth_Year" listesinden "1996" degeri secilir
* "tb_CreateAnAccount_Adress_FirstName" elementine "Hepsi" değeri yazilir
* "tb_CreateAnAccount_Adress_LastName" elementine "Express" değeri yazilir
* "tb_CreateAnAccount_Adress_Company" elementine "HepsiBurada" değeri yazilir
* "tb_CreateAnAccount_Adress_Adress" elementine "Kustepe Mah. Mecidiyeköy Yolu Cad. Trump Towers Kule 2 Kat:2 No:12" değeri yazilir
* "tb_CreateAnAccount_Adress_City" elementine "Istanbul" değeri yazilir
* "slt_CreateAnAccount_Adress_State" listesinden "1" degeri secilir
* "tb_CreateAnAccount_Adress_PostCode" elementine "34100" değeri yazilir
* "tb_CreateAnAccount_Adress_HomePhone" elementine "5555555555" değeri yazilir
* "tb_CreateAnAccount_Adress_MobilePhone" elementine "5555555555" değeri yazilir
* "tb_CreateAnAccount_Adress_FutureReference" elementine "TrumpTowers" değeri yazilir
* "btn_CreateAnAccount_Register" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=my-account" olması beklenir
* "btn_MyAccount_MyPersonalInformation" elementi görünene kadar beklenir
* "btn_MyAccount_MyPersonalInformation" elementi "MY PERSONAL INFORMATION" değerini içermektedir
* "btn_MyAccount_Dresses" elementinin uzerine gelinir
* "btn_MyAccount_Dresses_SummerDresses" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?id_category=11&controller=category" olması beklenir
* "btn_SummerDresses_FirstItem_Name" elementinin "text" degeri "itemNameAtSearch" degiskenine kaydedilir
* "btn_SummerDresses_FirstItem_Price" elementinin "text" degeri "itemPriceAtSearch" degiskenine kaydedilir
* "btn_SummerDresses_FirstItem" elementinin uzerine gelinir
* "btn_SummerDresses_FirstItem_AddToCart" elementine tıklanır
* "btn_AddtoCart_Cross" elementi görünene kadar beklenir
* "btn_AddtoCart_Cross" elementine tıklanır
* "btn_Cart_ItemQuantity" elementi görünene kadar beklenir
* "btn_Cart_ItemQuantity" elementi "1" değerini içermektedir
* "btn_CartView" elementinin uzerine gelinir
* "btn_Cart_ItemName" elementinin "title" degeri "itemNameAtCart" degiskenine kaydedilir
* "btn_Cart_ItemPrice" elementinin "text" degeri "itemPriceAtCart" degiskenine kaydedilir
* "itemNameAtSearch" ve "itemNameAtCart" değişkenlerinin değerleri birbirini icerir
* "itemPriceAtSearch" ve "itemPriceAtCart" değişkenlerinin değerleri birbirini icerir
* "btn_CartView_Checkout" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=order" olması beklenir
* "btn_CheckoutSummary_ProceedToCheckOut" elementi görünene kadar beklenir
* "btn_CheckoutSummary_ProceedToCheckOut" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=order&step=1" olması beklenir
* "btn_CheckoutAdress_ProceedToCheckOut" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=order" olması beklenir
* "btn_CheckoutShipping_AgreeForm" elementine tıklanır
* "btn_CheckoutShipping_ProceedToCheckOut" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=order&multi-shipping=" olması beklenir
* "btn_CheckoutPayment_Cheque" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?fc=module&module=cheque&controller=payment" olması beklenir
* "btn_CheckoutPayment_ConfirmOrder" elementine tıklanır
* "btn_CheckoutPayment_SuccessAlert" elementi görünene kadar beklenir
* "btn_CheckoutPayment_SuccessAlert" elementi "Your order on My Store is complete." değerini içermektedir
* "btn_Checkout_MyAccount" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=my-account" olması beklenir
* "btn_MyAccount_Orders" elementine tıklanır
* Mevcut sayfanin "http://automationpractice.com/index.php?controller=history" olması beklenir
* "10" saniye bekle
* "btn_Order_FirstOrder" elementi görünene kadar beklenir


HX Case Concept
-----------------------------------------------------------
tags:conceptUsingFeature
* Sign in” > “Create Account” seçeneği ile kullanıcı ve adres bilgileri girilerek yeni bir kullanıcı oluşturulur
* Anasayfada kullanıcının oluştuğu doğrulanır
* “DRESSES” > “SUMMER DRESSES” menusu seçilir ve açılan kategori sayfasından bir ürün Sepete eklenir. • “Summer” ürün araması gerçekleştirilir
* “Cart” > “Check Out” menusu ile Sepet görüntülenir, eklenen ürünler doğrulanır (Ürün sayısı, Ürün isimleri, fiyat bilgileri vb) ve “Proceed to checkout” seçeneği ile diğer adıma geçilir.
* Adres seçimi gerçekleştirilir ve “Proceed to checkout” seçeneği ile sonraki adıma geçilir
* Açılan “Shipping” ekranında Kargo seçeneği ve hizmet şartları kabul edilir ve “Proceed to checkout” seçeneği ile “Payment” adımına geçilir
* Ödeme ekranında herhangi çek ödeme yöntemi seçilerek sipariş tamamlanır
* Oluşturulan sipariş kullanıcı menusunde bulunan “Order history and details” ekranından kontrol edilir