# Paracrawl
Crawl Multi Language News Website Content like VovWorld, VNAnet, VietNamPlus, QuanDoiNhanDan etc

This tools made by me with help of instructors **DR. Tran Hong Viet** (thviet79) and **masters Bui Van Tan**

This tool is by for Window and Linux users, it purpose to crawl rare Language such as **Laotian, Khmer** and popular language like **Chinese, English** etc you can add more if you want

> **Folders and Files organize**

For each website News you have 1 Folder, it contains link of categories manually collected in linkauto Folder. When the tool run it'll check this folder to get all the news link, title (and date) at first run time. At second time etc, it with check the latest news of the website then add it to resource to save time (time it's **knowledge** and **sleep** =) ).

> **Detect Bilingual News**

As you know news has **title and date (some not in numeric format)**. Beacause news is very lagre resource so compare them is very time consuming. So we set ***date range*** around 15 days or 1 month. It reduce a lot of unnecessary canculating. With title we **translate it from Machine translation** (googleApi etc) to translate it to **Vietnamese**. After that titles will be tokenize by **VNCoreNLP** then use **TF-IDF** and **stop words** to remove words has no meaning like và ( and), or (hoặc), về (about) etc then compare titles similar or not.

> **TF-IDF & Stop Words Results**

**Bag of words**

S1: “chuyển_đổi số : động_lực phát_triển”

S2: “chuyển_đổi sang kỹ_thuật_số : động_lực để phát_triển”

chuyển_đổi | kỹ_thuật_số | động_lực | phát_triển| số |
--- | --- | --- | --- | --- |
2 | 1 | 2 | 2 | 1 |

**S1 bag of words**

chuyển_đổi| động_lực | phát_triển| số |
--- | --- | --- | --- |
2 | 2 | 2 | 1 |

**S2 bag of words**

chuyển_đổi | kỹ_thuật_số | động_lực | phát_triển|
--- | --- | --- | --- |
2 | 1 | 2 | 2 |

**TF-IDF Vector** 

Text |chuyển_đổi | kỹ_thuật_số | động_lực | phát_triển| số |
--- |--- | --- | --- | --- | --- |
S1 | 1| -1 | 1 | 1 | 0.30 |
S2 | 1 | 0.30 | 1 | 1 | -1 |


Origin title | Translated title | Score |
--- | --- | --- | 
chủ_tịch quốc_hội lào đánh_giá cao các sáng_kiến và đề_xuất của việt_nam tại aipa 42  | chủ_tịch quốc_hội lào biểu_dương các sáng_kiến và đề_xuất của việt_nam tại aipa 42 | 0.9022|
quan_hệ nga mỹ : nhân_tố duy_trì sự ổn_định chiến_lược | quan_hệ nga mỹ : ổn_định chiến_lược| 0.7676183059241082
giá_trị của tư_tưởng hồ_chí_minh về chủ_nghĩa_xã_hội và con đường đi lên chủ_nghĩa_xã_hội ở việt_nam | những giá_trị của quan_niệm hồ_chí_minh về chủ_nghĩa_xã_hội và con đường đi lên chủ_nghĩa_xã_hội ở việt_nam | 0.7612
cộng_đồng quốc_tế ủng_hộ các giải_pháp của việt_nam trong vấn_đề biển đông 	| cộng_đồng quốc_tế ủng_hộ các biện_pháp của việt_nam trong vấn_đề biển đông 	| 0.7612
chuyển_đổi số : động_lực phát_triển |chuyển_đổi sang kỹ_thuật_số : động_lực để phát_triển| 0.7425

Our solution working prety well on finding bilingual news but there are many shortcomings, that I'll describe at below

> **Problem**
  
  **Machine Translation Tool**

  **Similar meaning words and TF-IDF **
  
  Origin title | Translated title | Bilingual |
--- | --- | --- |
 khai_mạc ngày hội giao_lưu văn_hoá thể_thao và du_lịch các dân_tộc_thiểu_số các tỉnh vùng biên_giới việt_nam lào  | vovworld_các tỉnh biên_giới việt_lào đã thống_nhất giao_lưu văn_hoá thể_thao và du_lịch với đồng_bào các dân_tộc | True
 lễ hồi_hương đưa_tiễn hài_cốt quân_tình_nguyện và chuyên_gia việt_nam hy_sinh tại lào |  lễ viếng 25 chuyên_gia quân_nhân việt_nam hy_sinh tại lào| True
 hội_thảo hệ_thống phát_triển liên_hợp_quốc và quan_hệ với việt_nam | hội_thảo quan_hệ nga asean vai_trò của việt_nam tại liên_bang nga | False
 khai_mạc hội_nghị bộ_trưởng kinh_tế asean lần thứ 51  | hội_nghị bộ_trưởng kinh_tế asean lần thứ 37| False
  
