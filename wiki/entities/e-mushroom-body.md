---
title: 蕈狀體（mushroom body）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, mb-learning]
confidence: high
---

# 蕈狀體（mushroom body）

## 是什麼

果蠅腦中負責把「聞到什麼」和「好事或壞事」連起來的構造，簡稱 MB。中文也有人譯作「蘑菇體」，本庫一律寫「蕈狀體」。[[s-minnick-2026-untrained-connectome]] 在一個整腦模擬中切除它：果蠅走路完全正常，卻再也走不到氣味源，可見它在該模型中的角色是替行為定方向，不是驅動行走本身。本庫各篇來源都把它當成嗅覺學習發生的地方。它由三種神經元的纖維交織而成：

- **Kenyon 細胞**（[[e-kenyon-cell]]，KC）：蕈狀體的主體神經元，負責代表氣味。
- **多巴胺神經元**（[[e-dopaminergic-neuron]]，DAN）：送來懲罰或獎賞訊號。
- **蕈狀體輸出神經元**（[[e-mbon]]，MBON）：讀取 KC 的訊號，影響行為。

**結構**（依 [[s-tomchik-2009-camp-dynamics]] 的讀前說明與 [[s-hige-2015-heterosynaptic-plasticity]]）：

| 部位 | 是什麼 |
|---|---|
| 萼部（calyx） | KC 的樹突（接收訊號的分枝）所在處，嗅覺投射神經元（projection neuron, PN；把嗅覺訊號從觸角葉送進來的神經元）在這裡把氣味交給 KC |
| 葉（lobe） | KC 的軸突（送出訊號的長纖維）成束形成的分枝。α/β 型與 α′/β′ 型 KC 的軸突分岔成往上的垂直葉（α、α′）與往內的水平葉（β、β′）；γ 型 KC 只有水平的 γ 葉 |
| 區室（compartment） | 葉沿長度切成的段落。依 Hige 2015 所引 Aso et al. 2014a，共 15 個互不重疊的區室（見 [[numbers]]），每一格各配一型 DAN 與一型 MBON；Handler 2019 的描述是「一小群 DAN 的軸突加一到兩個 MBON 的樹突」共同定義一格（兩篇計數的單位不同：前者講「型」，後者講「個」，原文沒有進一步對照）。γ 葉上的 γ1–γ5 就是區室編號 |

一條 KC 軸突會依序穿過好幾個區室，沿途與各區室的 MBON 接觸（Hige 2015）。區室為什麼重要、能不能獨立改變，見 [[c-mb-compartment]]，本頁只講結構。

MBON 與 DAN 都以所在區室命名，例如 MBON-γ1pedc（γ1pedc 區的輸出神經元）、PPL1-γ1pedc（PPL1 這群 DAN 中支配 γ1pedc 區的那一型）。有些名稱串了兩段，例如 γ2α′1、α′2α2；※ 推論：表示該細胞跨 γ2 與 α′1 兩個區室，但本庫各篇都沒有說明命名規則。字尾 pedc 與 MBON-α2sc 的 sc 是什麼意思，各篇原文都沒有直接寫出，但 [[s-aso-2014-mb-architecture]] 給了依據（※ 推論）：pedc 指柄（pedunculus）遠端的核心，因為該篇寫 MBON-γ1pedc>α/β 的樹突「在同側的 γ1 與柄核心」；sc 指表層（surface）與核心層（core），因為該篇寫 MBON-α2sc 取 α2 的表層與核心層、MBON-α2p3p 取後層（p）。兩者都是從該篇的描述推回字母，論文沒有明文定義縮寫。（Aso 2016 圖 3F 圖說把 γ1pedc 拆成 γ1 與 pedc 兩個區室。）

## 版本與規模

- **區室**：葉上共 15 個（γ、α′/β′、α/β 各 5 個），另有柄遠端核心 pedc 由一型 MBON 與一型 DAN 專屬支配——庫內被反覆引用的這個數字，第一出處就是本庫收錄的 [[s-aso-2014-mb-architecture]]（Hige 2015、Aso 2016、Felsenberg 2017 都引它，見 [[numbers]]）。區室再依「哪幾型 KC 的軸突經過」細分成基本分區，全葉 37 個。[[s-pribbenow-2022-postsynaptic-plasticity]] 寫「至少 15 個功能區室」，與此一致，但它量化受體分布的熱圖橫軸只有 13 格（⚠️ 單篇自身不一致，見該來源頁）。
- **KC 總數**：約 2,000 顆（每半腦）。[[s-aso-2014-mb-architecture]] 自己計數（nlsLacZ 標核、電腦輔助計數），七型加總 2,015。Aso 2016 第 57 行「~2000 Kenyon cells」（引 Laurent & Naraghi 1994、Perez-Orive et al. 2002）與 Cohn 2015 第 132 行「~2,000 KCs」都是引言中的轉述。
- **各型 KC 的數量**（[[s-aso-2014-mb-architecture]] 表 1、圖 6、圖 7，每半腦）：γd 約 75、γ main 約 600、α′/β′ap 約 210、α′/β′m 約 140、α/βp 約 90、α/βs 約 500、α/βc 約 400。
- **MBON 與 DAN**：葉上 21 型 MBON 共 34 顆、20 型 DAN 約 130 顆（PAM 14 型、PPL1 6 型），加上約 2,000 顆 KC，全葉約 2,200 個神經元（[[s-aso-2014-mb-architecture]]）。
- **其他**：一型 MBON 在一到兩個區室中接收約 90 到約 2000 顆 KC 的輸入，一顆 KC 沿軸突與 5–6 型 MBON 形成途經式突觸（Aso 2016 引 Aso et al. 2009、2014a；收斂比的上下限 2300:1 與 90:1 出自 [[s-aso-2014-mb-architecture]] 圖 12B，前提是「每顆 KC 在它經過的每個分區都形成突觸」）。

## 庫內誰用了它

| 來源 | 量了蕈狀體的哪一部分 | 空間解析度 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | α 葉末端、α′ 葉、γ 葉（KC 軸突）與萼部（KC 樹突）；另量萼部的 PN 軸突、α 葉上 DPM 神經元（一對支配整個蕈狀體葉部的大型神經元）的神經突。在萼部噴乙醯膽鹼（嗅覺訊號傳給 KC 時用的物質，用來模擬氣味），在垂直葉噴多巴胺（模擬懲罰） | 到「葉」為止，沒有分區室 |
| [[s-gervasi-2010-pka-dynamics]] | 萼部與 α、β、γ 葉（KC 軸突與樹突，活體）；α′、β′ 葉量不到 | 整條葉（每個量測範圍平均數百顆細胞的纖維，不分區室） |
| [[s-hige-2015-heterosynaptic-plasticity]] | 三個區室的 MBON：γ1pedc、γ2α′1、α2（MBON-α2sc）；另以鈣影像量 KC 細胞體層 | 區室 |
| [[s-handler-2019-dopamine-receptor-timing]] | γ 葉的 γ2、γ4、γ5 區室的 MBON；KC 軸突在 γ4/γ5 區室的 cAMP（多巴胺受體被活化後在細胞內升高的訊號分子）與內質網鈣（細胞內儲鈣小倉庫放出的鈣）；γ2/γ3 的比較在補充圖 S6D–F：？待查。乙醯膽鹼以離子導入（用電流把藥從玻璃細針推出）送到萼部模擬氣味 | 區室 |
| [[s-cohn-2015-coordinated-neuromodulation]] | γ 葉的 γ2–γ5：KC 末梢、DAN 末梢、MBON（γ1 沒有常規成像） | 區室；KC 末梢到單一突觸小結 |
| [[s-aso-2016-dan-cell-type-rules]] | 六組品系的 DAN 支配的區室（正文說 15 格中的 11 格，圖上數得 12 格）；只有行為 | 區室（由品系的解剖推回） |
| [[s-ichinose-2015-reward-recurrent-circuit]] | α1 區室，以及 MB 外的 SMP、SIP、SLP（PAM-α1 樹突與 MBON-α1 末梢相遇處） | 區室；光學超解析解剖 |
| [[s-felsenberg-2017-re-evaluation]] | α／α′ 葉的 V2 群 MBON、γ2α′1、γ5 的 PAM 末梢；PPL1 的細胞體 | 區室 |
| [[s-felsenberg-2018-memory-extinction]] | γ1pedc（MVP2）、β′2（M4β′）、γ5（M6）；γ4、γ5、β′2p、β′2m 的 PAM 末梢；全腦電顯影像 FAFB 上的突觸 | 區室；電顯到單一突觸 |
| [[s-huang-2024-dopamine-memory-dynamics]] | 五型 PPL1（γ1pedc、γ2α′1、α′2α2、α3、α′3）支配的八個區室（圖 1a，原文未逐一列出八格）與六型 MBON（γ1pedc>α/β、γ2α′1、α2sc、α′2、α3、α′3m）；活體電壓成像量單次放電。模型只取 γ1、α2、α3 三個模組，接線依連結體 hemibrain v1.2.1 | 區室；MBON 在區室內的樹突拍攝（放電從軸突反向傳進樹突，延伸圖 2，所以樹突上看到的是整顆細胞的放電） |
| [[s-mao-2009-dopaminergic-neuron-types]] | 解剖：全蕈狀體的 DAN 支配（含萼部，在此之前一般認為萼部沒有多巴胺）；功能：垂直葉四段的 DAN 末梢鈣 | 光學切片的「段」（α／α′ 尖端、上段、下段連交界），段的邊界沒有定義；共軛焦 20× |
| [[s-aso-2014-mb-architecture]] | 葉、柄與萼部的**全部**細胞組成與分區：7 型 KC、21 型 MBON、20 型 DAN，以及它們如何鋪成 15 個區室與 37 個基本分區 | 共軛焦 20× 全腦加 63× 局部，對位到標準腦 JFRC2013（0.38 µm 等向體素）；細胞計數用 0.1 µm 等向體素；神經氈共存的分析以 3.8 µm 立方塊為單位 |
| [[s-aso-2014-mbon-valence]] | 不量蕈狀體，而是逐型操作：15 個區室（加 pedc）的 MBON 以光活化或阻斷測行為 | 細胞型別（由品系的解剖推回） |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | 九個區室的 DAN 與 KC：γ1–γ5、β′1、β′2、α1/α′1，加上作者自訂的 junction（各葉在根部的交會處） | 區室（目視圈出的 ROI）；共軛焦 20×、每秒 5 張 |
| [[s-eschbach-2021-learned-innate-valence-integration]] | **幼蟲**蕈狀體的輸出端：24 型 MBON 與它們的全部下游；KC 只作為被整體活化或阻斷的對象 | 電顯重建 3.8 × 3.8 × 50 nm；功能量測以單一細胞型為單位 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | 乙醯膽鹼受體次單元與 Dlg 在各區室的分布（熱圖 13 格）；M4/6 的樹突與軸突、α′3 區室 | 區室；受體影像體素 123 × 123 × 500 nm |

## 已知的問題

- **各篇量的部位幾乎不重疊。** Tomchik 量 α、α′ 葉與萼部；Hige 量 γ1pedc 與 α2；Handler 量 γ4/γ5；Cohn 量 γ2–γ5；Ichinose 操作 α1；Felsenberg 兩篇操作 α/α′ 葉的 V2、γ2α′1、γ1pedc、β′2、γ5；Huang 2024 量 PPL1 支配的 γ1pedc、γ2α′1、α′2α2、α3、α′3，沒有量 PAM 支配的區室。把各篇的結論接在一起時，等於假設不同葉、不同區室遵守同樣的規則，而 Hige 2015 自己就發現 γ1 與 α2 的誘發門檻（要多少「氣味＋多巴胺」的配對才會讓突觸變弱）不同。
- **Tomchik 2009 的空間解析度只到葉。** 它看到 cAMP 的協同（乙醯膽鹼與多巴胺一起給時，cAMP 上升比兩者分開給的總和還大）出現在葉部，但無法回答協同是否只出現在收到多巴胺的那一個區室（該來源頁「未來」一節）。
- **幼蟲的蕈狀體不照成蟲的分法。** [[s-eschbach-2021-learned-innate-valence-integration]] 用的是萼、柄、側附區、垂直葉、垂直葉上段、內側葉這一套幼蟲區室，與成蟲 γ、α′/β′、α/β 三條葉的 15 格不對應；幼蟲 MBON 只有 24 型。引用幼蟲的結果時要註明是哪一套座標。
- **光學顯微鏡層級的「相鄰」不等於相連。** [[s-aso-2014-mb-architecture]] 自陳它給的是 potential connections：兩條纖維落在同一塊 3.8 µm 立方體內就算共存，而 3.8 µm 比一個突觸大兩個數量級。
- ⚠️ **Handler 2019 方法中區室的近端／遠端標示自相矛盾**：同一段先說「近端的 γ2/γ3」，三行後又說「遠端（γ2/γ3）與近端（γ4/γ5）」（單篇不一致，見該來源頁 3.5 節）。近、遠是相對於什麼，原文也沒說；哪一組在近端，本頁不補。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-mbon]]
- 概念：[[c-mb-compartment]]、[[c-kc-mbon-plasticity]]、[[c-ex-vivo-explant]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-eschbach-2021-learned-innate-valence-integration]]、[[s-pribbenow-2022-postsynaptic-plasticity]]
