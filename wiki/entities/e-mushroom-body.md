---
title: 蘑菇體（mushroom body）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: high
---

# 蘑菇體（mushroom body）

## 是什麼

果蠅腦中負責把「聞到什麼」和「好事或壞事」連起來的構造，簡稱 MB。本庫各篇來源都把它當成嗅覺學習發生的地方。它由三種神經元的纖維交織而成：

- **Kenyon 細胞**（[[e-kenyon-cell]]，KC）：蘑菇體的主體神經元，負責代表氣味。
- **多巴胺神經元**（[[e-dopaminergic-neuron]]，DAN）：送來懲罰或獎賞訊號。
- **蘑菇體輸出神經元**（[[e-mbon]]，MBON）：讀取 KC 的訊號，影響行為。

**結構**（依 [[s-tomchik-2009-camp-dynamics]] 的讀前說明與 [[s-hige-2015-heterosynaptic-plasticity]]）：

| 部位 | 是什麼 |
|---|---|
| 萼部（calyx） | KC 的樹突（接收訊號的分枝）所在處，嗅覺投射神經元（projection neuron, PN；把嗅覺訊號從觸角葉送進來的神經元）在這裡把氣味交給 KC |
| 葉（lobe） | KC 的軸突（送出訊號的長纖維）成束形成的分枝。α/β 型與 α′/β′ 型 KC 的軸突分岔成往上的垂直葉（α、α′）與往內的水平葉（β、β′）；γ 型 KC 只有水平的 γ 葉 |
| 區室（compartment） | 葉沿長度切成的段落。依 Hige 2015 所引 Aso et al. 2014a，共 15 個互不重疊的區室（見 [[numbers]]），每一格各配一型 DAN 與一型 MBON；Handler 2019 的描述是「一小群 DAN 的軸突加一到兩個 MBON 的樹突」共同定義一格（兩篇計數的單位不同：前者講「型」，後者講「個」，原文沒有進一步對照）。γ 葉上的 γ1–γ5 就是區室編號 |

一條 KC 軸突會依序穿過好幾個區室，沿途與各區室的 MBON 接觸（Hige 2015）。區室為什麼重要、能不能獨立改變，見 [[c-mb-compartment]]，本頁只講結構。

MBON 與 DAN 都以所在區室命名，例如 MBON-γ1pedc（γ1pedc 區的輸出神經元）、PPL1-γ1pedc（PPL1 這群 DAN 中支配 γ1pedc 區的那一型）。有些名稱串了兩段，例如 γ2α′1、α′2α2；※ 推論：表示該細胞跨 γ2 與 α′1 兩個區室，但本庫各篇都沒有說明命名規則。字尾 pedc 與 MBON-α2sc 的 sc 是什麼意思，本庫各篇原文都沒有解釋：？待查（Aso 2016 圖 3F 圖說把 γ1pedc 拆成 γ1 與 pedc 兩個區室）。

## 版本與規模

- **區室**：葉上共 15 個（Hige 2015、Aso 2016、Felsenberg 2017 都引 Aso et al. 2014a，見 [[numbers]]）。
- **KC 總數**：約 2,000 顆（Aso 2016 第 57 行「~2000 Kenyon cells」，引 Laurent & Naraghi 1994、Perez-Orive et al. 2002；Cohn 2015 第 132 行「~2,000 KCs」）。兩篇都是引言中的轉述，不是自己計數；被引用的兩篇是否量的是果蠅，本庫沒有查證：？待查。
- **其他**：一型 MBON 在一到兩個區室中接收約 90 到約 2000 顆 KC 的輸入，一顆 KC 沿軸突與 5–6 型 MBON 形成途經式突觸（Aso 2016 引 Aso et al. 2009、2014a）。各型 KC 的數量：？待查。

## 庫內誰用了它

| 來源 | 量了蘑菇體的哪一部分 | 空間解析度 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | α 葉末端、α′ 葉、γ 葉（KC 軸突）與萼部（KC 樹突）；另量萼部的 PN 軸突、α 葉上 DPM 神經元（一對支配整個蘑菇體葉部的大型神經元）的神經突。在萼部噴乙醯膽鹼（嗅覺訊號傳給 KC 時用的物質，用來模擬氣味），在垂直葉噴多巴胺（模擬懲罰） | 到「葉」為止，沒有分區室 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 三個區室的 MBON：γ1pedc、γ2α′1、α2（MBON-α2sc）；另以鈣影像量 KC 細胞體層 | 區室 |
| [[s-handler-2019-dopamine-receptor-timing]] | γ 葉的 γ2、γ4、γ5 區室的 MBON；KC 軸突在 γ4/γ5 區室的 cAMP（多巴胺受體被活化後在細胞內升高的訊號分子）與內質網鈣（細胞內儲鈣小倉庫放出的鈣）；γ2/γ3 的比較在補充圖 S6D–F：？待查。乙醯膽鹼以離子導入（用電流把藥從玻璃細針推出）送到萼部模擬氣味 | 區室 |
| [[s-cohn-2015-coordinated-neuromodulation]] | γ 葉的 γ2–γ5：KC 末梢、DAN 末梢、MBON（γ1 沒有常規成像） | 區室；KC 末梢到單一突觸小結 |
| [[s-aso-2016-dan-cell-type-rules]] | 六組品系的 DAN 支配的區室（正文說 15 格中的 11 格，圖上數得 12 格）；只有行為 | 區室（由品系的解剖推回） |
| [[s-ichinose-2015-reward-recurrent-circuit]] | α1 區室，以及 MB 外的 SMP、SIP、SLP（PAM-α1 樹突與 MBON-α1 末梢相遇處） | 區室；光學超解析解剖 |
| [[s-felsenberg-2017-re-evaluation]] | α／α′ 葉的 V2 群 MBON、γ2α′1、γ5 的 PAM 末梢；PPL1 的細胞體 | 區室 |
| [[s-felsenberg-2018-memory-extinction]] | γ1pedc（MVP2）、β′2（M4β′）、γ5（M6）；γ4、γ5、β′2p、β′2m 的 PAM 末梢；全腦電顯影像 FAFB 上的突觸 | 區室；電顯到單一突觸 |

## 已知的問題

- **各篇量的部位幾乎不重疊。** Tomchik 量 α、α′ 葉與萼部；Hige 量 γ1pedc 與 α2；Handler 量 γ4/γ5；Cohn 量 γ2–γ5；Ichinose 操作 α1；Felsenberg 兩篇操作 α/α′ 葉的 V2、γ2α′1、γ1pedc、β′2、γ5。把各篇的結論接在一起時，等於假設不同葉、不同區室遵守同樣的規則，而 Hige 2015 自己就發現 γ1 與 α2 的誘發門檻（要多少「氣味＋多巴胺」的配對才會讓突觸變弱）不同。
- **Tomchik 2009 的空間解析度只到葉。** 它看到 cAMP 的協同（乙醯膽鹼與多巴胺一起給時，cAMP 上升比兩者分開給的總和還大）出現在葉部，但無法回答協同是否只出現在收到多巴胺的那一個區室（該來源頁「未來」一節）。
- ⚠️ **Handler 2019 方法中區室的近端／遠端標示自相矛盾**：同一段先說「近端的 γ2/γ3」，三行後又說「遠端（γ2/γ3）與近端（γ4/γ5）」（單篇不一致，見該來源頁 3.5 節）。近、遠是相對於什麼，原文也沒說；哪一組在近端，本頁不補。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]、[[e-mbon]]
- 概念：[[c-mb-compartment]]、[[c-kc-mbon-plasticity]]、[[c-ex-vivo-explant]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
