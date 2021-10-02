# Paracrawl
Crawl Multi Language News Website Content like VovWorld, VNAnet, VietNamPlus, QuanDoiNhanDan etc

This tools made by me with help of instructors **DR. Tran Hong Viet** (thviet79) and **masters Bui Van Tan**

This tool is by for Window and Linux users, it purpose to crawl rare Language such as **Laotian, Khmer** and popular language like **Chinese, English** etc you can add more if you want

> **Folders and Files organize**

For each website News you have 1 Folder, it contains link of categories manually collected in linkauto Folder. When the tool run it'll check this folder to get all the news link, title (and date) at first run time. At second time etc, it with check the latest news of the website then add it to resource to save time (time it's **knowledge** and **sleep** =) ).

> **Detect Bilingual News**

As you know news has **title and date (some not in numeric format)**. Beacause news is very lagre resource so compare them is very time consuming. So we set ***date range*** around 15 days or 1 month. It reduce a lot of unnecessary canculating. With title we **translate it from Machine translation** (googleApi etc) to translate it to **Vietnamese**. After that titles will be tokenize by **VNCoreNLP** then use **TF-IDF** and **stop words** to remove words has no meaning like và ( and), or (hoặc), về (about) etc then compare titles similar or not.

> **TF-IDF & Stop Words Results**

Origin title | Translated title | Score |
--- | --- | --- |
chủ_tịch quốc_hội lào đánh_giá cao các sáng_kiến và đề_xuất của việt_nam tại aipa 42  | chủ_tịch quốc_hội lào biểu_dương các sáng_kiến và đề_xuất của việt_nam tại aipa 42 | 0.9022|
chuyển_đổi số : động_lực phát_triển |chuyển_đổi sang kỹ_thuật_số : động_lực để phát_triển| 0.8179
quan_hệ nga mỹ : nhân_tố duy_trì sự ổn_định chiến_lược | quan_hệ nga mỹ : ổn_định chiến_lược| 0.7676183059241082
giá_trị của tư_tưởng hồ_chí_minh về chủ_nghĩa_xã_hội và con đường đi lên chủ_nghĩa_xã_hội ở việt_nam | những giá_trị của quan_niệm hồ_chí_minh về chủ_nghĩa_xã_hội và con đường đi lên chủ_nghĩa_xã_hội ở việt_nam | 0.7612
cộng_đồng quốc_tế ủng_hộ các giải_pháp của việt_nam trong vấn_đề biển đông 	| cộng_đồng quốc_tế ủng_hộ các biện_pháp của việt_nam trong vấn_đề biển đông 	| 0.7612

Our solution working prety well on finding bilingual news but there are many shortcomings, that I'll describe at below

> **Problem**
  
  **Machine Translation Tool**

  **Similar meaning words**

