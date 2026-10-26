# 果蠅蘑菇體研究知識庫：索引

**[[syn-changelog|更新履歷]]**：這座知識庫怎麼長成現在的樣子，以及它更正過自己幾次
**[[syn-contradictions|矛盾與空缺]]**：論文之間說法不同、等人裁決的地方，以及沒有人做過的實驗

範圍是果蠅（*Drosophila*）蘑菇體（mushroom body）的研究。蘑菇體是果蠅腦中負責「把氣味和好壞結果連起來」的區域，是研究學習與記憶最常用的模型之一。目前 **9 篇來源**、4 條主題、14 個概念、26 個實體、2 個綜述，分屬兩個研究問題群。

**怎麼讀這份索引。** 第一層是**研究問題群**，第二層是**主題**。主題頁（`t-`）回答「這批論文對這件事說了什麼、彼此怎麼對話」，用白話寫成，是讀者的入口。概念頁（`c-`）與實體頁（`e-`）掛在主題底下，供查詞。來源頁（`s-`）是一篇論文一頁，含科普文、專業文與每張主圖的解讀。完整的來源清單在文末。

**先讀什麼。** 不熟蘑菇體的讀者，依序讀 [[e-mushroom-body]]、[[e-kenyon-cell]] 兩頁短的參考頁，再讀 [[t-timing-rules]] 與 [[t-dopamine-to-plasticity]]，最後讀第二個問題群的 [[t-memory-updating]] 與 [[t-mbon-dan-feedback]]。在 GitHub 網頁上，頁面之間的 `[[ ]]` 連結不能點；要點開某一頁，請開 [README](README.md)（也就是 GitHub 上 repo 首頁下方的說明），那裡有一份每頁都能點的目錄。

---

## 學習的訊號機制：多巴胺如何改變 KC→MBON 突觸

蘑菇體的學習模型是：每個氣味活化一小群 Kenyon 細胞（KC），所以「哪一群 KC 在活動」就代表是哪個氣味；多巴胺神經元（DAN）帶來好壞訊號（在實驗裡常用電擊當懲罰、用糖當獎賞）；兩者同時出現時，KC 與輸出神經元（MBON，它的活動推動果蠅靠近或走開）之間的接點（突觸）會變強或變弱。蘑菇體沿長度分成一格一格的區室，每格由一型 DAN 支配、一型 MBON 讀取。最早收錄的三篇都在這條線上，分別量了 KC 內部的化學訊號、輸出突觸的電流、以及受體與時序的關係；第二批的 Cohn 2015 直接看了 KC 送訊號那一端的鈣，Aso 2016 在行為上比較了各型多巴胺神經元的時序規則。2026-10-26 收錄的 Tully 1985 年代最早、全文沒有提到蘑菇體：它建立了庫內多篇沿用的 T 迷宮「氣味—電擊」學習測驗，用它量了電擊要在氣味之後多快來才學得到，並比較了 *rutabaga* 等學習突變株的記憶曲線。這些突變株壞掉的基因都在製造或分解 cAMP 的路徑上，但這是作者引用前人的生化結果，本篇自己沒有量 cAMP。

### [[t-timing-rules]]｜先後與間隔：氣味和多巴胺的時序如何決定學到什麼

同一個氣味、同一次懲罰，只差氣味和懲罰誰先誰後、隔多久，學到的東西就不一樣。「時間窗」指氣味與懲罰最多能相隔多久，仍然學得到。幾篇論文在不同的層次上量它，得到的長短不同：

- 行為上（看果蠅學不學得到）：以數十秒計。只活化一型多巴胺神經元時，相隔數十秒甚至會決定學到的是躲開還是喜歡。
- KC 內的化學訊號：以數秒計。
- 單一突觸上：以一秒計，見下一句。

突觸上，多巴胺比氣味早約一秒到時，突觸變強；兩者同時、或多巴胺比氣味晚到時，突觸變弱。突觸變強或變弱，對應果蠅學到躲開還是喜歡，要看那一格的 MBON 推動的是靠近還是走開，所以同一個方向的突觸改變，在不同格會變成相反的行為。各篇計算「相隔多久」的起算點不同，數字不能直接比。**懲罰比氣味先到時，果蠅是沒學到、還是學到相反的偏好，各篇說法不一；多巴胺神經元在完全沒有氣味時被活化，會不會讓突觸變強（這不符合「要配對才會學」的模型），兩篇說法也不同。兩者都列為待裁決。**

- 概念：[[c-cs-us-timing]]、[[c-coincidence-detection]]、[[c-kc-mbon-plasticity]]、[[c-us-substitution]]、[[c-performance-index]]
- 實體：[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-kenyon-cell]]
- 來源：[[s-tully-1985-classical-conditioning]]、[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-handler-2019-dopamine-receptor-timing]]

### [[t-dopamine-to-plasticity]]｜從多巴胺到突觸改變：KC 軸突怎麼讀出增強訊號

多巴胺神經元送來的多巴胺量，不論氣味先還是多巴胺先都一樣（Handler 2019 量過）；差別在 KC 的軸突收到多巴胺之後，細胞內啟動了哪些化學反應。兩篇給了不同的答案：

- **問題的起點（Tully 1985）：** 只有行為與遺傳。學不好的突變株，壞掉的基因都落在製造或分解 cAMP 的路徑上；但 *rutabaga* 突變株缺了被認為負責偵測「氣味與懲罰同時到」的酵素活性，卻仍學得到一些，作者因此指出，以海兔（*Aplysia*）提出的「這個酵素是學習必需」的模型解釋不了果蠅。
- **較早的答案（Tomchik 2009）：** *rutabaga* 基因製造的一個酵素負責製造 cAMP（一種細胞內的訊號分子）。它要同時收到兩種訊號才大量工作：氣味讓 KC 活動時流進細胞的鈣，以及多巴胺。所以它像一個「兩者都到才響」的偵測器；作者還發現，只有氣味先、多巴胺後時，cAMP 才會多出來。
- **較新的答案（Handler 2019）：** KC 上有兩種多巴胺受體，各接一條路徑。一條製造 cAMP，讓突觸變弱；這篇量到的 cAMP 不論誰先都會上升。另一條讓內質網（細胞內儲存鈣的構造）放出鈣，讓突觸變強，只在多巴胺先到時才發生。所以氣味先到時只有變弱的那條在作用；多巴胺先到時兩條都在作用，變強的那條勝出。

**兩篇對「cAMP 分不分得出先後」說法相反，列為待裁決**（Handler 2019 正文沒有點名 *rutabaga*，它量到的 cAMP 是不是同一個酵素製造的，沒有交代）。另外兩點：學習造成的突觸改變主要限在一格（區室）之內，但 Cohn 2015 發現活化一格的多巴胺神經元時，別格的 MBON 反應也會小幅下降；Cohn 2015 也直接看到 KC 送訊號那一端（末梢）的鈣會隨多巴胺改變，不過那是沒有配對氣味時的結果。**配對之後末梢怎麼變沒有人量過，所以學習的改變發生在 KC 這一側（突觸前）還是 MBON 那一側（突觸後），仍沒有答案。**

- 概念：[[c-camp-signaling]]、[[c-coincidence-detection]]、[[c-mb-compartment]]、[[c-kc-mbon-plasticity]]
- 實體：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-epac-camp-sensor]]
- 概念（第二批）：[[c-presynaptic-calcium]]、[[c-ex-vivo-explant]]、[[c-whole-cell-patch-clamp]]、[[c-odor-generalization]]
- 實體（第二批）：[[e-dopamine-receptor]]、[[e-mbon-gamma4]]、[[e-mbon-gamma1pedc]]、[[e-ppl1-gamma1pedc]]
- 實體（2026-10-26）：[[e-rutabaga]]
- 來源：[[s-tully-1985-classical-conditioning]]、[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2018-memory-extinction]]、[[s-handler-2019-dopamine-receptor-timing]]

---

## 記憶寫入之後：鞏固、更新與迴路回饋

記憶寫下之後並沒有定案。它要經過一段時間才穩定（鞏固）；再遇到同一個氣味卻沒有獎賞或懲罰時，它會被改寫（消退、再鞏固）。上一節的圖像是單向的：氣味從 KC 流到 MBON，DAN 從旁改寫兩者之間的接點。這些過程卻需要反方向的路：MBON 回頭改變 DAN 的活動。2026-10-25 第二批收錄的五篇（Cohn 2015、Ichinose 2015、Aso 2016、Felsenberg 2017、Felsenberg 2018）大多落在這裡。2026-10-26 收錄的 Tully 1985 提供了最早的行為資料：學會之後只聞氣味、不再挨電（消退），要 20 輪（約 1 小時）才讓分數減半；先學「甲是壞的」再學「乙是壞的」，學習分數（0＝沒學到、1＝全部躲開被電的氣味）只有 0.26（單學一次約 0.89），果蠅只略偏向較近的那一次。

### [[t-memory-updating]]｜記憶怎麼被改寫：消退、再鞏固與新舊記憶並存

訓練時果蠅會先後聞兩個氣味：一個配糖或電擊（受訓氣味），另一個不配（對照氣味）。學會之後，再聞受訓氣味卻沒有糖或電擊，記憶會變弱，這叫消退。另一種情況是再聞對照氣味，記憶反而被叫出來、重新穩定一次，這叫再鞏固。變弱的原因，是舊記憶被擦掉了，還是另外寫下一筆方向相反的新記憶把它蓋過去？DAN 依細胞體的位置分成兩大群，簡稱 PPL1 與 PAM：PPL1 群的活動通常代表懲罰，PAM 群通常代表獎賞。同一團隊的兩篇（Felsenberg 2017、2018）互為鏡像：獎賞記憶的消退要靠 PPL1 群（「該來的糖沒來」被當成壞事記下），懲罰記憶的消退要靠 PAM 群（「該來的電擊沒來」被當成好事記下）；後一篇（Felsenberg 2018）並看到舊的痕跡還在，新的痕跡寫在另一格。另一篇（Aso 2016）只用光叫醒單一型多巴胺神經元，發現各格改寫記憶的規則不同：有的格只記得最新的一組「氣味—結果」配對，有的格能同時記住兩組、而且不容易被抹掉。**「抹除」與「被蓋過」在行為上分不出來，只有一篇直接量過神經痕跡；而且兩篇鏡像實驗消退的記憶，一個是訓練後 3 小時、一個是訓練後 30 分鐘，不是條件對齊的比較。**

- 概念：[[c-memory-extinction]]、[[c-memory-consolidation]]、[[c-spaced-training]]、[[c-performance-index]]
- 實體：[[e-shibire-ts]]、[[e-t-maze]]、[[e-olfactory-arena]]、[[e-mb504b]]、[[e-r58e02]]、[[e-mbon-gamma5beta2a]]、[[e-mbon-gamma2alpha1]]、[[e-ppl1-gamma2alpha1]]
- 來源：[[s-tully-1985-classical-conditioning]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]

### [[t-mbon-dan-feedback]]｜輸出神經元回頭指揮多巴胺神經元：MBON→DAN 回饋迴路

教科書上的蘑菇體是單向的：氣味從 KC 流到輸出神經元，多巴胺神經元從旁改寫兩者之間的接點。四篇論文各找到反方向的路，主要有三種：

1. 同一格裡的迴路（Ichinose 2015）：α1 格的 MBON 回頭讓同格的 DAN 更活躍，糖吃完之後獎賞訊號還能延續一段時間；少了這段延續，就形成不了長期記憶。
2. 一型牽動全體（Cohn 2015）：活化任一型 MBON，各格 DAN 的活動都跟著改變。
3. 預期落空時的跨格回饋（Felsenberg 2017、2018）：一格的 MBON 去叫醒另一格、代表相反好壞的 DAN，用來寫下消退記憶。

**這些路的位置、作用時機與證據強度都不同，多數只有解剖上的相鄰，或在取出的腦（離體製備）裡的少量紀錄，沒有一條在活的果蠅身上被直接量到正在作用。** 其中一處，兩篇說法相反：活化 γ2 格的 MBON 之後，同一格的 DAN 是變安靜（Cohn 2015）還是被叫醒（Felsenberg 2017），列為待裁決。

- 概念：[[c-memory-consolidation]]、[[c-memory-extinction]]、[[c-ex-vivo-explant]]
- 實體：[[e-pam-alpha1]]、[[e-mbon-gamma2alpha1]]、[[e-ppl1-gamma2alpha1]]、[[e-mbon-gamma5beta2a]]、[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-p2x2]]
- 來源：[[s-cohn-2015-coordinated-neuromodulation]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]

---

## 實驗工具（實體頁）

不屬於單一主題、但讀實驗細節時常要查的工具：

- [[e-gcamp]]：鈣感測器，神經元活動時會變亮。庫內各篇用了六種版本，各自的亮度變化（ΔF/F：變化量除以基線亮度）不能跨篇比較
- [[e-epac-camp-sensor]]：cAMP 感測器
- [[e-cschrimson]]：紅光活化的光遺傳通道，用來以光代替懲罰或獎賞
- [[e-split-gal4]]：只在少數幾型神經元表現的驅動品系，決定「活化了誰」。個別品系另有頁：[[e-mb099c]]、[[e-mb504b]]、[[e-r58e02]]、[[e-th-gal4]]、[[e-c739-gal4]]；其中 MB099C 與 R58E02 標記了哪些神經元，各篇說法不同，列為待裁決
- [[e-p2x2]]：遇到 ATP 就打開的通道，用化學方法活化神經元
- [[e-shibire-ts]]：升溫時暫時阻斷神經元輸出的工具，用來問「哪段時間需要哪群神經元」
- [[e-t-maze]]、[[e-olfactory-arena]]：兩種量果蠅氣味偏好的行為裝置；T 迷宮的古典制約版本來自 Tully 1985
- [[c-ex-vivo-explant]]、[[c-whole-cell-patch-clamp]]：取出整顆腦做實驗、以電極記錄單顆神經元的兩種方法

---

## 全部來源（依發表年）

每行最後的日期是本庫收錄日，不是發表日。

- [[s-tully-1985-classical-conditioning]] — Tully & Quinn, *J Comp Physiol A*：建立 T 迷宮的氣味—電擊古典制約測驗，量了時序、消退、非聯結對照與學習突變株的記憶曲線；全文不涉及蘑菇體 · 2026-10-26
- [[s-tomchik-2009-camp-dynamics]] — Tomchik & Davis, *Neuron*：在離體腦中直接看到 KC 軸突裡的 cAMP 協同依賴 *rutabaga* 與先後順序 · 2026-10-25
- [[s-hige-2015-heterosynaptic-plasticity]] — Hige et al., *Neuron*：活體記錄到多巴胺讓 KC→MBON 突觸長期抑制，區室專一、依賴順序 · 2026-10-25
- [[s-cohn-2015-coordinated-neuromodulation]] — Cohn, Morantte & Ruta, *Cell*：多巴胺神經元整群協調活動；同一條 KC 軸突在各格的末梢鈣不同；沒有氣味時活化多巴胺神經元讓突觸變強 · 2026-10-25
- [[s-ichinose-2015-reward-recurrent-circuit]] — Ichinose et al., *eLife*：MBON-α1 與 PAM-α1 形成迴圈，訓練後第一小時需要它，獎賞的長期記憶才會形成 · 2026-10-25
- [[s-aso-2016-dan-cell-type-rules]] — Aso & Rubin, *eLife*：各型多巴胺神經元寫入與更新記憶的規則不同；同一型依時序寫入相反的記憶 · 2026-10-25
- [[s-felsenberg-2017-re-evaluation]] — Felsenberg et al., *Nature*：再聞受訓氣味不給糖會消退、再聞對照氣味會再鞏固，兩者走不同的迴路 · 2026-10-25
- [[s-felsenberg-2018-memory-extinction]] — Felsenberg et al., *Cell*：懲罰記憶的消退由獎賞型多巴胺神經元寫下一筆相反的記憶，新舊兩筆在一顆叫 M6 的輸出神經元（讀取 γ5 格）上整合 · 2026-10-25
- [[s-handler-2019-dopamine-receptor-timing]] — Handler et al., *Cell*：DopR1 與 DopR2 兩條路徑讓同一突觸依先後變弱或變強 · 2026-10-25

---

## 登記簿

- [[numbers]]：數字登記簿。每個具體數字的定義與量測方式
- [[intake]]：收錄登記簿。`papers/` 裡每份 PDF 的處理狀態
- [[log]]：日誌
