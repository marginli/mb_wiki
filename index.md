# 果蠅學習與記憶知識庫：索引

**[[syn-changelog|更新履歷]]**：這座知識庫怎麼長成現在的樣子，以及它更正過自己幾次
**[[syn-contradictions|矛盾與空缺]]**：論文之間說法不同、等人裁決的地方，以及沒有人做過的實驗

範圍是果蠅（*Drosophila*）的學習與記憶研究，以及蕈狀體（mushroom body）本身的研究（2026-11-12 由只收蕈狀體擴大而來）。蕈狀體是果蠅腦中負責「把氣味和好壞結果連起來」的區域，是研究學習與記憶最常用的模型，也是目前已收論文的共同主軸；蕈狀體以外的學習記憶研究（例如中央複合體的空間學習、求偶制約、幼蟲的學習）收到論文後會各自成為新的研究問題群，**第一個這樣的問題群已在 2026-11-21 成立**（下方的「視覺的學習與記憶」，由中央複合體的視覺位置學習開張）。目前 **27 篇來源**、7 條主題、24 個概念、52 個實體、2 個綜述，分屬三個研究問題群。

**怎麼讀這份索引。** 第一層是**研究問題群**，第二層是**主題**。主題頁（`t-`）回答「這批論文對這件事說了什麼、彼此怎麼對話」，用白話寫成，是讀者的入口。概念頁（`c-`）與實體頁（`e-`）掛在主題底下，供查詞。來源頁（`s-`）是一篇論文一頁，含科普文、專業文與每張主圖的解讀。完整的來源清單在文末。

**先讀什麼。** 不熟蕈狀體的讀者，依序讀 [[e-mushroom-body]]、[[e-kenyon-cell]] 兩頁短的參考頁，再讀 [[t-timing-rules]] 與 [[t-dopamine-to-plasticity]]，最後讀第二個問題群的 [[t-memory-updating]] 與 [[t-mbon-dan-feedback]]。想知道本庫目前最沒有共識的地方長什麼樣子，讀第三個問題群的 [[t-visual-learning-circuits]]——它記錄的是一個三方不一致、而且還不能裁決的爭點。在 GitHub 網頁上，頁面之間的 `[[ ]]` 連結不能點；要點開某一頁，請開 [README](README.md)（也就是 GitHub 上 repo 首頁下方的說明），那裡有一份每頁都能點的目錄。

---

## 學習的訊號機制：多巴胺如何改變 KC→MBON 突觸

蕈狀體的學習模型是：每個氣味活化一小群 Kenyon 細胞（KC），所以「哪一群 KC 在活動」就代表是哪個氣味；多巴胺神經元（DAN）帶來好壞訊號（在實驗裡常用電擊當懲罰、用糖當獎賞）；兩者同時出現時，KC 與輸出神經元（MBON，它的活動推動果蠅靠近或走開）之間的接點（突觸）會變強或變弱。蕈狀體沿長度分成一格一格的區室，每格由一型 DAN 支配、一型 MBON 讀取。最早收錄的三篇都在這條線上，分別量了 KC 內部的化學訊號、輸出突觸的電流、以及受體與時序的關係；第二批的 Cohn 2015 直接看了 KC 送訊號那一端的鈣，Aso 2016 在行為上比較了各型多巴胺神經元的時序規則。2026-10-26 收錄的 Tully 1985 年代最早、全文沒有提到蕈狀體：它建立了庫內多篇沿用的 T 迷宮「氣味—電擊」學習測驗，用它量了電擊要在氣味之後多快來才學得到，並比較了 *rutabaga* 等學習突變株的記憶曲線。這些突變株壞掉的基因都在製造或分解 cAMP 的路徑上，但這是作者引用前人的生化結果，Tully 1985 自己沒有量 cAMP。 2026-11-12 收錄的 Tumkaya 2025 走到這條線的另一端：它把氣味和懲罰（或獎賞）都換成光，整場訓練沒有任何自然刺激，果蠅照樣學得起來，可見「兩條路徑同時有活動」就足以指揮記憶形成；同一篇也發現，ORN 放電的精細節奏果蠅學不起來。

### [[t-timing-rules]]｜先後與間隔：氣味和多巴胺的時序如何決定學到什麼

同一個氣味、同一次懲罰，只差氣味和懲罰誰先誰後、隔多久，學到的東西就不一樣。「時間窗」指氣味與懲罰最多能相隔多久，仍然學得到。幾篇論文在不同的層次上量它，得到的長短不同：

- 行為上（看果蠅學不學得到）：以數十秒計。只活化一型多巴胺神經元時，相隔數十秒甚至會決定學到的是躲開還是喜歡。
- KC 內的化學訊號：以數秒計。
- 單一突觸上：以一秒計，見下一句。

突觸上，多巴胺比氣味早約一秒到時，突觸變強；兩者同時、或多巴胺比氣味晚到時，突觸變弱。突觸變強或變弱，對應果蠅學到躲開還是喜歡，要看那一格的 MBON 推動的是靠近還是走開，所以同一個方向的突觸改變，在不同格會變成相反的行為。各篇計算「相隔多久」的起算點不同，數字不能直接比。**懲罰比氣味先到時，果蠅是沒學到、還是學到相反的偏好，各篇說法不一；多巴胺神經元在完全沒有氣味時被活化，會不會讓突觸變強（這不符合「要配對才會學」的模型），兩篇說法也不同。兩者都列為待裁決。**

- 概念：[[c-cs-us-timing]]、[[c-coincidence-detection]]、[[c-kc-mbon-plasticity]]、[[c-us-substitution]]、[[c-performance-index]]
- 實體：[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-kenyon-cell]]
- 來源：[[s-tully-1985-classical-conditioning]]、[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tumkaya-2025-synthetic-memory-inception]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-kaldun-2025-dop1r2-memory-phases]]、[[s-vogt-2014-shared-visual-olfactory-circuits]]

### [[t-dopamine-to-plasticity]]｜從多巴胺到突觸改變：KC 軸突怎麼讀出增強訊號

多巴胺神經元送來的多巴胺量，不論氣味先還是多巴胺先都一樣（Handler 2019 量過）；差別在 KC 的軸突收到多巴胺之後，細胞內啟動了哪些化學反應。兩篇給了不同的答案：

- **問題的起點（Tully 1985）：** 只有行為與遺傳。學不好的突變株，壞掉的基因都落在製造或分解 cAMP 的路徑上；但 *rutabaga* 突變株缺了被認為負責偵測「氣味與懲罰同時到」的酵素活性，卻仍學得到一些，作者因此指出，以海兔（*Aplysia*）提出的「這個酵素是學習必需」的模型解釋不了果蠅。
- **較早的答案（Tomchik 2009）：** *rutabaga* 基因製造的一個酵素負責製造 cAMP（一種細胞內的訊號分子）。它要同時收到兩種訊號才大量工作：氣味讓 KC 活動時流進細胞的鈣，以及多巴胺。所以它像一個「兩者都到才響」的偵測器；作者還發現，只有氣味先、多巴胺後時，cAMP 才會多出來。
- **較新的答案（Handler 2019）：** KC 上有兩種多巴胺受體，各接一條路徑。一條製造 cAMP，讓突觸變弱；這篇量到的 cAMP 不論誰先都會上升。另一條讓內質網（細胞內儲存鈣的構造）放出鈣，讓突觸變強，只在多巴胺先到時才發生。所以氣味先到時只有變弱的那條在作用；多巴胺先到時兩條都在作用，變強的那條勝出。

- **往下游量一步（Gervasi 2010）：** 在活的果蠅裡看 cAMP 打開的下一個酵素 PKA。多巴胺只在 α 葉打開 PKA，拿掉分解 cAMP 的 Dunce 後就打開所有葉，作者據此主張 *dunce* 突變的問題在 cAMP 的「位置」而非「量」。它也重做了配對的放大，但 *rutabaga* 突變只測了配對組；與 Tomchik 2009 另有兩處相反，列為待裁決

**兩篇對「cAMP 分不分得出先後」說法相反，列為待裁決**（Handler 2019 正文沒有點名 *rutabaga*，它量到的 cAMP 是不是同一個酵素製造的，沒有交代）。另外兩點：學習造成的突觸改變主要限在一格（區室）之內，但 Cohn 2015 發現活化一格的多巴胺神經元時，別格的 MBON 反應也會小幅下降；Cohn 2015 也直接看到 KC 送訊號那一端（末梢）的鈣會隨多巴胺改變，不過那是沒有配對氣味時的結果。**配對之後末梢怎麼變沒有人量過，所以學習的改變發生在 KC 這一側（突觸前）還是 MBON 那一側（突觸後），仍沒有答案。**

- 概念：[[c-camp-signaling]]、[[c-coincidence-detection]]、[[c-mb-compartment]]、[[c-kc-mbon-plasticity]]、[[c-sparse-coding]]
- 實體：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-epac-camp-sensor]]
- 概念（第二批）：[[c-presynaptic-calcium]]、[[c-ex-vivo-explant]]、[[c-whole-cell-patch-clamp]]、[[c-odor-generalization]]
- 實體（第二批）：[[e-dopamine-receptor]]、[[e-mbon-gamma4]]、[[e-mbon-gamma1pedc]]、[[e-ppl1-gamma1pedc]]
- 實體（2026-10-26）：[[e-rutabaga]]
- 2026-11-12 因 Gervasi 2010 新開：[[e-dunce]]、[[e-238y-gal4]]、[[c-octopamine-reward-signal]]
- 來源：[[s-tully-1985-classical-conditioning]]、[[s-tomchik-2009-camp-dynamics]]、[[s-gervasi-2010-pka-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2018-memory-extinction]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tumkaya-2025-synthetic-memory-inception]]、[[s-minnick-2026-untrained-connectome]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-burke-2012-octopamine-dopamine-reward]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-yamada-2023-second-order-conditioning]]、[[s-kaldun-2025-dop1r2-memory-phases]]、[[s-vogt-2014-shared-visual-olfactory-circuits]]

---

## 記憶寫入之後：鞏固、更新與迴路回饋

記憶寫下之後並沒有定案。它要經過一段時間才穩定（鞏固）；再遇到同一個氣味卻沒有獎賞或懲罰時，它會被改寫（消退、再鞏固）。上一節的圖像是單向的：氣味從 KC 流到 MBON，DAN 從旁改寫兩者之間的接點。這些過程卻需要反方向的路：MBON 回頭改變 DAN 的活動。2026-10-25 第二批收錄的五篇（Cohn 2015、Ichinose 2015、Aso 2016、Felsenberg 2017、Felsenberg 2018）大多落在這裡。2026-10-26 收錄的 Tully 1985 提供了最早的行為資料：學會之後只聞氣味、不再挨電（消退），要 20 輪（約 1 小時）才讓分數減半；先學「甲是壞的」再學「乙是壞的」，學習分數（0＝沒學到、1＝全部躲開被電的氣味）只有 0.26（單學一次約 0.89），果蠅只略偏向較近的那一次。

### [[t-memory-updating]]｜記憶怎麼被改寫：消退、再鞏固與新舊記憶並存

訓練時果蠅會先後聞兩個氣味：一個配糖或電擊（受訓氣味），另一個不配（對照氣味）。學會之後，再聞受訓氣味卻沒有糖或電擊，記憶會變弱，這叫消退。另一種情況是再聞對照氣味，記憶反而被叫出來、重新穩定一次，這叫再鞏固。變弱的原因，是舊記憶被擦掉了，還是另外寫下一筆方向相反的新記憶把它蓋過去？DAN 依細胞體的位置分成兩大群，簡稱 PPL1 與 PAM：PPL1 群的活動通常代表懲罰，PAM 群通常代表獎賞。同一團隊的兩篇（Felsenberg 2017、2018）互為鏡像：獎賞記憶的消退要靠 PPL1 群（「該來的糖沒來」被當成壞事記下），懲罰記憶的消退要靠 PAM 群（「該來的電擊沒來」被當成好事記下）；後一篇（Felsenberg 2018）並看到舊的痕跡還在，新的痕跡寫在另一格。另一篇（Aso 2016）只用光叫醒單一型多巴胺神經元，發現各格改寫記憶的規則不同：有的格只記得最新的一組「氣味—結果」配對，有的格能同時記住兩組、而且不容易被抹掉。**「抹除」與「被蓋過」在行為上分不出來，只有一篇直接量過神經痕跡；而且兩篇鏡像實驗消退的記憶，一個是訓練後 3 小時、一個是訓練後 30 分鐘，不是條件對齊的比較。**

- 概念：[[c-memory-extinction]]、[[c-memory-consolidation]]、[[c-spaced-training]]、[[c-performance-index]]
- 實體：[[e-shibire-ts]]、[[e-t-maze]]、[[e-olfactory-arena]]、[[e-mb504b]]、[[e-r58e02]]、[[e-mbon-gamma5beta2a]]、[[e-mbon-gamma2alpha1]]、[[e-ppl1-gamma2alpha1]]
- 來源：[[s-tully-1985-classical-conditioning]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-yamada-2023-second-order-conditioning]]、[[s-kaldun-2025-dop1r2-memory-phases]]

### [[t-mbon-dan-feedback]]｜輸出神經元回頭指揮多巴胺神經元：MBON→DAN 回饋迴路

教科書上的蕈狀體是單向的：氣味從 KC 流到輸出神經元，多巴胺神經元從旁改寫兩者之間的接點。五篇論文各找到反方向的路，主要有四種：

1. 同一格裡的迴路（Ichinose 2015）：α1 格的 MBON 回頭讓同格的 DAN 更活躍，糖吃完之後獎賞訊號還能延續一段時間；少了這段延續，就形成不了長期記憶。
2. 一型牽動全體（Cohn 2015）：活化任一型 MBON，各格 DAN 的活動都跟著改變。
3. 預期落空時的跨格回饋（Felsenberg 2017、2018）：一格的 MBON 去叫醒另一格、代表相反好壞的 DAN，用來寫下消退記憶。
4. 短期記憶打開長期記憶的閘門（Huang 2024）：γ1pedc 格的 MBON 平常抑制 α3 格的 DAN；訓練讓這條抑制放鬆，α3 的 DAN 才對受訓氣味放電，長期改變才寫進 α3。

**這些路的位置、作用時機與證據強度都不同，多數只有解剖上的相鄰，或在取出的腦（離體製備）裡的少量紀錄。只有第 4 種在活的果蠅學習時量到 DAN 隨 MBON 改變（電壓成像），但阻斷用的是從發育期就作用的毒素，成像與行為也是不同的果蠅。** 其中一處，兩篇說法相反：活化 γ2 格的 MBON 之後，同一格的 DAN 是變安靜（Cohn 2015）還是被叫醒（Felsenberg 2017），列為待裁決。

- 概念：[[c-memory-consolidation]]、[[c-memory-extinction]]、[[c-ex-vivo-explant]]
- 實體：[[e-pam-alpha1]]、[[e-mbon-gamma2alpha1]]、[[e-ppl1-gamma2alpha1]]、[[e-mbon-gamma5beta2a]]、[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-p2x2]]、[[e-ppl1-alpha3]]、[[e-ppl1-alpha2alpha2]]、[[e-mbon-alpha2sc]]
- 來源：[[s-cohn-2015-coordinated-neuromodulation]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-burke-2012-octopamine-dopamine-reward]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-yamada-2023-second-order-conditioning]]、[[s-aso-2023-upwind-neurons]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-li-2020-mb-connectome]]


### [[t-mbon-to-action]]｜學到的價值怎麼變成動作：MBON 下游的讀出

MBON 的活動怎麼變成果蠅的動作？成蟲的逐型活化顯示推動靠近或走開大致依傳遞物質分邊，而迎風神經元把兩型 MBON 的訊號整合成迎風移動；二選一的分數和迎風行為可以分開，所以「學到了」和「怎麼走過去」是兩件事。幼蟲的通則與成蟲不同。

- 來源：[[s-aso-2014-mbon-valence]]、[[s-aso-2023-upwind-neurons]]、[[s-yamada-2023-second-order-conditioning]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-tully-1985-classical-conditioning]]、[[s-vogt-2014-shared-visual-olfactory-circuits]]、[[s-li-2020-mb-connectome]]

### [[t-innate-learned-integration]]｜先天與習得的價值在哪裡整合

天生的好惡與學來的好惡在哪裡加總？三篇給了三個位置：神經氈的匯聚區（解剖推測）、成蟲的多巴胺神經元（電壓成像）、幼蟲 MBON 下游的匯聚神經元（電顯追蹤）。三者不互斥，也沒有一篇在同一個實驗裡同時測過兩處。

- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-aso-2023-upwind-neurons]]

---

## 視覺的學習與記憶

**果蠅記住看到的東西時用的是哪一塊腦，本庫目前的來源給出互不相容的答案。** 這是 2026-11-21 成立的問題群（tag `visual-learning`），也是本庫第一個不以蕈狀體為中心的問題群。本庫原有的二十餘篇幾乎都以氣味為條件刺激，多巴胺、KC 與 MBON 的規則全是在嗅覺裡量出來的；把「要記住的東西」換成顏色或地點之後，連「蕈狀體參不參與」都還沒有定論。這一群目前有四篇（2026-11-24 加入蕈狀體連結體），所以它記錄的是爭點而不是結論。

### [[t-visual-learning-circuits]]｜果蠅用哪一塊腦記住看到的東西

一篇說視覺**位置**學習完全不需要蕈狀體、必要節點在橢球體的 R1 環；一篇說**顏色**記憶需要蕈狀體的 γ 葉、而且走的是同一批多巴胺神經元與同一個受體；兩篇在連結體裡確認視覺訊息確實進得了蕈狀體——一份用 hemibrain 半腦（[[s-li-2020-mb-connectome]]，約 8% 的 Kenyon 細胞以視覺為主，而且腹側與背側副萼走的是直接與間接兩條相反的路），一份用 FlyWire 全腦——但兩篇都完全沒有測功能，而且它們對視覺 Kenyon 細胞的突觸形態說法相反（[[syn-contradictions]] 1.15）。三者的作業、操作範圍與讀數刻度都不同，所以現在還不能說誰對；**不能裁決的理由本身就是這一頁的主要內容**（登記為 [[syn-contradictions]] 1.13）。另一個關聯的分歧是「視覺 Kenyon 細胞有幾顆」：光學計數約 75 顆、連結體計數 147 顆，差近一倍（1.14），而在它被釐清之前，「某個遺傳操作有沒有蓋到視覺 KC」就沒有分母可算。

- 概念：[[c-acquisition-vs-retrieval]]、[[c-neurotransmitter-prediction]]、[[c-sparse-coding]]、[[c-performance-index]]、[[c-us-substitution]]
- 實體：[[e-ellipsoid-body]]、[[e-kir2-1]]、[[e-color-conditioning-arena]]、[[e-dumb2]]、[[e-mb247-gal4]]、[[e-mb008b]]
- 來源：[[s-ofstad-2011-visual-place-learning]]、[[s-vogt-2014-shared-visual-olfactory-circuits]]、[[s-ganguly-2024-visual-inputs-to-kc]]、[[s-li-2020-mb-connectome]]

---

## 氣味代碼的刻板性與個體化

**同一個氣味在每隻果蠅的嗅葉點亮同一組嗅小球，在蕈狀體卻點亮一群至今找不出固定樣式的 Kenyon 細胞。** 這是 2026-11-24 成立的問題群（tag `mb-odor-coding`），由使用者讀 [[s-aso-2014-mb-architecture]] 的科普文時提出的兩個問題逼出來：「真的每隻果蠅都不一樣嗎」與「學習會不會改變 PN 到 KC 的接線」。前者使本庫發現自己把一句三手轉述寫成了定論，後者使本庫發現庫內 28 篇來源沒有一篇測過這件事。這一群關心的是**學習之前**的那張代碼表——它在哪一層固定、在哪一層失去固定、以及固定與否如何限制了「能從一份連結體推論到哪裡」。

### [[t-stereotypy-to-individualization]]｜氣味代碼在哪一層不再固定

嗅葉那一層固定得很徹底（氣味對應一組位置固定的嗅小球，PN 的形態在個體間可疊合，被認為是基因決定的），而蕈狀體的萼「丟棄」了這個秩序：每顆 Kenyon 細胞從約 200 條投射神經元裡抓 6 條左右，知道一條推不出其餘。但「丟棄」不等於均勻亂灑——[[s-li-2020-mb-connectome]] 實測出結構，而結構在「KC 型別 × 嗅小球」這個層級（相對幅度 9–14%，γ 型看不到偏離），不在單顆 KC 的組合；[[s-ganguly-2024-visual-inputs-to-kc]] 在視覺側連隨機與刻板兩個模型都分不開。秩序在輸出端以另一種形式回來：**回來的是 21 型 MBON「誰讀哪一段、推動靠近還是走開」的固定分工，不是內容**——同一型 MBON 的氣味反應在天真個體之間就已經分歧，而且被歸因於可塑性。學習寫在 KC→MBON 那一層而不是接線上（[[s-hige-2015-heterosynaptic-plasticity]] 直接量到 KC 的代碼沒動、MBON 的輸入降約九成），但「接線不會因學習而變」在本庫是**沒有人測過**，不是已被否證。

- 概念：[[c-sparse-coding]]、[[c-mb-compartment]]、[[c-valence-coding]]
- 實體：[[e-kenyon-cell]]、[[e-mbon]]、[[e-accessory-calyx]]
- 來源：[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-li-2020-mb-connectome]]、[[s-ganguly-2024-visual-inputs-to-kc]]

---

## 實驗工具（實體頁）

不屬於單一主題、但讀實驗細節時常要查的工具：

- [[e-gcamp]]：鈣感測器，神經元活動時會變亮。庫內各篇用了六種版本，各自的亮度變化（ΔF/F：變化量除以基線亮度）不能跨篇比較
- [[e-epac-camp-sensor]]：cAMP 感測器
- [[e-cschrimson]]：紅光活化的光遺傳通道，用來以光代替懲罰或獎賞
- [[e-split-gal4]]：只在少數幾型神經元表現的驅動品系，決定「活化了誰」。個別品系另有頁：[[e-ok107-gal4]]、[[e-c305a-gal4]]、[[e-vt1211]]、[[e-mb099c]]、[[e-mb504b]]、[[e-r58e02]]、[[e-th-gal4]]、[[e-c739-gal4]]、[[e-238y-gal4]]、[[e-mb247-gal4]]、[[e-mb008b]]；其中 MB099C 與 R58E02 標記了哪些神經元，各篇說法不同，列為待裁決
- [[e-p2x2]]：遇到 ATP 就打開的通道，用化學方法活化神經元
- [[e-tnt]]：破傷風毒素輕鏈，永久阻斷神經元的化學傳遞（發育期就開始，不能只在某段時間關掉）
- [[e-dtrpa1]]：升溫時打開的通道，用加熱活化神經元，常用來以熱代替電擊或糖
- [[e-gal80ts]]：溫度控制的開關，讓基因操作只在成蟲期生效，避開發育期的影響
- [[e-kir2-1]]：讓神經元難以放電的鉀通道，用來長期靜音一群細胞；它關的是放電，不是傳遞物質的釋放
- [[e-dumb2]]：多巴胺受體 DopR 的無效突變，插入片段帶 UAS，所以同一個等位基因既是突變、又能被叫回來表現
- [[e-shibire-ts]]：升溫時暫時阻斷神經元輸出的工具，用來問「哪段時間需要哪群神經元」
- [[e-t-maze]]、[[e-olfactory-arena]]：兩種量果蠅氣味偏好的行為裝置；T 迷宮的古典制約版本來自 Tully 1985
- [[e-color-conditioning-arena]]：四象限顏色制約場地，地板同時是螢幕與透明的電擊格柵，讓顏色制約能用與氣味制約相同的懲罰
- [[c-ex-vivo-explant]]、[[c-whole-cell-patch-clamp]]：取出整顆腦做實驗、以電極記錄單顆神經元的兩種方法
- [[c-acquisition-vs-retrieval]]：只在訓練時或只在測驗時阻斷，用來分辨「記憶寫不進去」與「記憶讀不出來」
- [[c-neurotransmitter-prediction]]：由電顯影像預測突觸用哪一種傳遞物質；連結體研究的「興奮或抑制」多半來自它，而它是預測不是量測
- [[e-ellipsoid-body]]：中央複合體裡的環狀構造，本庫唯一一個「不經過蕈狀體的學習」的必要腦區
- [[e-hemibrain]]、[[e-neuprint]]：半邊中央腦的電顯連結體資料集，與查詢它的網頁介面與資料庫。兩頁分工：資料集涵蓋什麼、缺什麼看前者，怎麼問、問法強加了什麼限制看後者
- [[e-fafb]]、[[e-catmaid]]：另一份成年果蠅全腦的電顯**影像體積**（不是連結體）與追蹤它的平台；庫內多篇在 hemibrain 查不到的東西靠它補
- [[e-nblast]]：比對兩顆神經元形態像不像的演算法，連結體研究拿它分亞型與跨資料集配對；它量的是形狀，不是功能
- [[e-accessory-calyx]]、[[e-visual-projection-neuron]]、[[e-lvin]]：三個副萼，以及把視覺訊息送進去的兩類神經元（直接送來的投射神經元，與轉一手的局部中間神經元）

---

## 全部來源（依發表年）

每行最後的日期是本庫收錄日，不是發表日。同一年有多篇時依刊出或接受日期排（Vogt 2014 在 2014-08 刊出，兩篇 Aso 2014 都在 2014-12；Ganguly 2024 於 2024-06 接受，Huang 2024 於 2024-07 線上先行）。

- [[s-tully-1985-classical-conditioning]] — Tully & Quinn, *J Comp Physiol A*：建立 T 迷宮的氣味—電擊古典制約測驗，量了時序、消退、非聯結對照與學習突變株的記憶曲線；全文不涉及蕈狀體 · 2026-10-26
- [[s-ofstad-2011-visual-place-learning]] — Ofstad, Zuker & Reiser, *Nature*：自製熱—視覺競技場，證明果蠅能用遠處視覺地標記住一個地點；靜音橢球體 R1 環讓位置學習歸零而氣味學習完好，靜音蕈狀體則相反 · 2026-11-21
- [[s-mao-2009-dopaminergic-neuron-types]] — Mao & Davis, *Front Neural Circuits*：單細胞選殖把支配蕈狀體的多巴胺神經元拆成八型，PPL1 五型各占垂直葉一段（舊名 MB-V1、MB-MV1、MB-MP1 的出處）；鈣成像看到各段對電擊與氣味的偏好不同 · 2026-11-13
- [[s-tomchik-2009-camp-dynamics]] — Tomchik & Davis, *Neuron*：在離體腦中直接看到 KC 軸突裡的 cAMP 協同依賴 *rutabaga* 與先後順序 · 2026-10-25
- [[s-gervasi-2010-pka-dynamics]] — Gervasi, Tchénio & Preat, *Neuron*：活果蠅 KC 內的 PKA 成像；多巴胺只在 α 葉打開 PKA，*dunce* 突變中打開全部；配對協同在 *rutabaga* 突變中消失，但只測了配對組 · 2026-11-12
- [[s-burke-2012-octopamine-dopamine-reward]] — Burke et al., *Nature*：獎賞訊號分層，章魚胺只傳遞糖的甜味那一份，經 PAM 多巴胺神經元上的受體接到多巴胺 · 2026-11-13
- [[s-vogt-2014-shared-visual-olfactory-circuits]] — Vogt et al., *eLife*：透明電擊格柵讓顏色制約與氣味制約用同一種懲罰；顏色記憶需要同一批 PAM／PPL1 多巴胺神經元、KC 的 DopR 與 γ 葉，α′/β′ 只管氣味 · 2026-11-21
- [[s-aso-2014-mb-architecture]] — Aso et al. 2014a, *eLife*：蕈狀體區室、DAN 與 MBON 型別與 split-GAL4 品系的解剖總圖譜，含新舊名對照表 · 2026-11-13
- [[s-aso-2014-mbon-valence]] — Aso et al. 2014b, *eLife*：逐型活化 MBON，推動靠近或走開依傳遞物質分邊；各種學習作業需要哪些 MBON · 2026-11-13
- [[s-hige-2015-heterosynaptic-plasticity]] — Hige et al., *Neuron*：活體記錄到多巴胺讓 KC→MBON 突觸長期抑制，區室專一、依賴順序 · 2026-10-25
- [[s-cohn-2015-coordinated-neuromodulation]] — Cohn, Morantte & Ruta, *Cell*：多巴胺神經元整群協調活動；同一條 KC 軸突在各格的末梢鈣不同；沒有氣味時活化多巴胺神經元讓突觸變強 · 2026-10-25
- [[s-ichinose-2015-reward-recurrent-circuit]] — Ichinose et al., *eLife*：MBON-α1 與 PAM-α1 形成迴圈，訓練後第一小時需要它，獎賞的長期記憶才會形成 · 2026-10-25
- [[s-aso-2016-dan-cell-type-rules]] — Aso & Rubin, *eLife*：各型多巴胺神經元寫入與更新記憶的規則不同；同一型依時序寫入相反的記憶 · 2026-10-25
- [[s-dylla-2017-trace-conditioning-dan-plasticity]] — Dylla et al., *Front Neural Circuits*：痕跡制約中 KC 與 DAN 的鈣反應改變，配對差異多來自不配對組下降 · 2026-11-13
- [[s-felsenberg-2017-re-evaluation]] — Felsenberg et al., *Nature*：再聞受訓氣味不給糖會消退、再聞對照氣味會再鞏固，兩者走不同的迴路 · 2026-10-25
- [[s-felsenberg-2018-memory-extinction]] — Felsenberg et al., *Cell*：懲罰記憶的消退由獎賞型多巴胺神經元寫下一筆相反的記憶，新舊兩筆在一顆叫 M6 的輸出神經元（讀取 γ5 格）上整合 · 2026-10-25
- [[s-handler-2019-dopamine-receptor-timing]] — Handler et al., *Cell*：DopR1 與 DopR2 兩條路徑讓同一突觸依先後變弱或變強 · 2026-10-25
- [[s-aso-2019-nitric-oxide-cotransmitter]] — Aso et al., *eLife*：部分 DAN 以一氧化氮為共同傳遞物，經 cGMP 路徑讓各區室的記憶動態不同 · 2026-11-13
- [[s-li-2020-mb-connectome]] — Li et al., *eLife*：把整塊蕈狀體的突觸層級接線圖攤開，重畫了三份清單——MBON 從 22 型變 34 型（14 型非典型，12 型首次描述）、Kenyon 細胞細分成 14 個亞型、15 個區室底下再拆出 40 個多巴胺神經元亞型；並第一次量化 MBON 回頭接 DAN 的規模與視覺怎麼進蕈狀體 · 2026-11-24
- [[s-eschbach-2021-learned-innate-valence-integration]] — Eschbach et al., *eLife*（幼蟲）：電顯追蹤 MBON 與側角輸出的下游，找到兩邊匯聚的神經元 · 2026-11-13
- [[s-pribbenow-2022-postsynaptic-plasticity]] — Pribbenow et al., *eLife*：MBON 上乙醯膽鹼受體次單元是獎賞與熟悉度記憶所需，給出突觸後可塑性的證據 · 2026-11-13
- [[s-aso-2023-upwind-neurons]] — Aso et al., *eLife*：迎風神經元整合 MBON-α1 與 MBON-α3 的輸入，把學到的氣味價值轉成迎風移動 · 2026-11-13
- [[s-yamada-2023-second-order-conditioning]] — Yamada et al., *eLife*：二階制約由 α1 的記憶經兩層中間神經元教別格的多巴胺神經元 · 2026-11-13
- [[s-ganguly-2024-visual-inputs-to-kc]] — Ganguly & Heckman et al., *Nat Commun*：在 FlyWire 全腦連結體裡逐顆數出視覺訊息怎麼進 Kenyon 細胞；名單固定、通道很窄、連法與隨機取樣相符，但完全沒有測功能 · 2026-11-21
- [[s-huang-2024-dopamine-memory-dynamics]] — Huang et al., *Nature*：電壓成像量到 PPL1 多巴胺神經元的單次放電，喜歡的氣味與糖讓牠們低於平常；短期記憶區的輸出神經元放鬆對長期記憶區多巴胺神經元的抑制，閘控長期記憶寫入；模型的雙向規則與 Hige 2015 牴觸（矛盾 1.9） · 2026-11-13
- [[s-tumkaya-2025-synthetic-memory-inception]] — Tumkaya et al., *iScience*：氣味與增強訊號都換成光，整場訓練沒有自然刺激，果蠅照樣形成記憶；ORN 放電的時間節奏則學不起來 · 2026-11-12
- [[s-kaldun-2025-dop1r2-memory-phases]] — Kaldun et al., *eLife*：細胞專一剔除多巴胺受體 Dop1R2，較晚的記憶在 α/β、α′/β′ 葉需要它 · 2026-11-13
- [[s-minnick-2026-untrained-connectome]] — Minnick et al., *arXiv* 預印本：把整份果蠅連結體原樣跑成脈衝網路並放進模擬身體；蕈狀體的學習讓趨近變成躲避，但原樣網路的 Kenyon 細胞不依賴氣味，那個學習並非聯結式 · 2026-11-12

---

## 登記簿

- [[numbers]]：數字登記簿。每個具體數字的定義與量測方式
- [[intake]]：收錄登記簿。`papers/` 裡每份 PDF 的處理狀態
- [[log]]：日誌
