# 果蠅蘑菇體研究知識庫：索引

**[[syn-changelog|更新履歷]]**：這座知識庫怎麼長成現在的樣子，以及它更正過自己幾次
**[[syn-contradictions|矛盾與空缺]]**：論文之間說法不同、等人裁決的地方，以及沒有人做過的實驗

範圍是果蠅（*Drosophila*）蘑菇體（mushroom body）的研究。目前 **3 篇來源**、2 條主題、7 個概念、8 個實體、2 個綜述。

**怎麼讀這份索引。** 第一層是**研究問題群**，第二層是**主題**。主題頁（`t-`）回答「這批論文對這件事說了什麼、彼此怎麼對話」，用白話寫成，是讀者的入口。概念頁（`c-`）與實體頁（`e-`）掛在主題底下，供查詞。來源頁（`s-`）是一篇論文一頁，含科普文、專業文與每張主圖的解讀。完整的來源清單在文末。

**先讀什麼。** 不熟蘑菇體的讀者，依序讀 [[e-mushroom-body]]、[[e-kenyon-cell]] 兩頁短的參考頁，再讀 [[t-timing-rules]] 與 [[t-dopamine-to-plasticity]]。在 GitHub 網頁上，頁面之間的 `[[ ]]` 連結不能點；要點開某一頁，請開 [README](README.md)（也就是 GitHub 上 repo 首頁下方的說明），那裡有一份每頁都能點的目錄。

---

## 學習的訊號機制：多巴胺如何改變 KC→MBON 突觸

蘑菇體的學習模型是：Kenyon 細胞（KC）代表氣味，多巴胺神經元（DAN）帶來好壞訊號，兩者的巧合改變 KC 與輸出神經元（MBON）之間的連結。本庫目前三篇都在這條線上，分別量了 KC 內部的化學訊號、輸出突觸的電流、以及受體與時序的關係。

### [[t-timing-rules]]｜先後與間隔：氣味和多巴胺的時序如何決定學到什麼

同一個氣味、同一次懲罰，只差氣味和懲罰誰先誰後、隔多久，學到的東西就不一樣。三篇在三個時間尺度上量這條規則。行為上，能不能學到的時間窗以數十秒計。KC 內的化學訊號以數秒計。突觸上，多巴胺比氣味早約一秒到時，突觸變強；兩者同時、或多巴胺比氣味晚到時，突觸變弱。三篇計算「氣味與懲罰相隔多久」時，有的從氣味開始算、有的從氣味結束算，所以數字不能直接比。**懲罰比氣味先到時，果蠅是沒學到、還是學到相反的偏好，三篇說法不一，列為待裁決。**

- 概念：[[c-cs-us-timing]]、[[c-coincidence-detection]]、[[c-kc-mbon-plasticity]]、[[c-us-substitution]]、[[c-performance-index]]
- 實體：[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-kenyon-cell]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]

### [[t-dopamine-to-plasticity]]｜從多巴胺到突觸改變：KC 軸突怎麼讀出增強訊號

不論氣味先還是多巴胺先，多巴胺神經元送來的多巴胺量都一樣；差別在 KC 的軸突接收到之後，細胞內啟動了哪些化學反應。較早的答案是 *rutabaga* 基因製造的一個酵素，它同時受鈣與多巴胺開啟，負責製造 cAMP 這種細胞內訊號分子。較新的答案是兩種多巴胺受體各接一條路徑：一條製造 cAMP，讓突觸變弱；一條讓細胞內的鈣倉庫放鈣，讓突觸變強。氣味先到時只有前一條開，突觸變弱；多巴胺先到時兩條都開，變強的那一條勝出。效果只限在蘑菇體的一小格（區室）內，不同格需要的刺激量不同。**改變發生在送訊號的 KC 那一側（突觸前），還是收訊號的 MBON 那一側（突觸後），三篇都沒有回答。**

- 概念：[[c-camp-signaling]]、[[c-coincidence-detection]]、[[c-mb-compartment]]、[[c-kc-mbon-plasticity]]
- 實體：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-epac-camp-sensor]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]

---

## 實驗工具（實體頁）

不屬於單一主題、但讀實驗細節時常要查的工具：

- [[e-gcamp]]：鈣感測器，神經元活動時會變亮。三篇用了四個不同版本，各自的「亮度變化百分比」（ΔF/F）不能跨篇比較
- [[e-epac-camp-sensor]]：cAMP 感測器
- [[e-cschrimson]]：紅光活化的光遺傳通道，用來以光代替懲罰或獎賞
- [[e-split-gal4]]：只在少數幾型神經元表現的驅動品系，決定「活化了誰」

---

## 全部來源（依發表年）

每行最後的日期是本庫收錄日，不是發表日。

- [[s-tomchik-2009-camp-dynamics]] — Tomchik & Davis, *Neuron*：在離體腦中直接看到 KC 軸突裡的 cAMP 協同依賴 *rutabaga* 與先後順序 · 2026-10-25
- [[s-hige-2015-heterosynaptic-plasticity]] — Hige et al., *Neuron*：活體記錄到多巴胺讓 KC→MBON 突觸長期抑制，區室專一、依賴順序 · 2026-10-25
- [[s-handler-2019-dopamine-receptor-timing]] — Handler et al., *Cell*：DopR1 與 DopR2 兩條路徑讓同一突觸依先後變弱或變強 · 2026-10-25

---

## 登記簿

- [[numbers]]：數字登記簿。每個具體數字的定義與量測方式
- [[intake]]：收錄登記簿。`papers/` 裡每份 PDF 的處理狀態
- [[log]]：日誌
