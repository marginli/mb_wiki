---
title: CsChrimson（紅光活化通道）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, mb-learning]
confidence: high
---

# CsChrimson（紅光活化通道）

## 是什麼

一種照紅光就打開、讓正離子流進細胞的通道蛋白（光敏感通道，opsin）。用驅動品系讓特定神經元製造它，紅光一照，那群神經元就放電。這種「用光控制神經元」的方法叫光遺傳（optogenetics）。在本庫，它主要用來直接活化 [[e-dopaminergic-neuron]]（DAN），代替電擊或糖水當作懲罰或獎賞（見 [[c-us-substitution]]）；Felsenberg 2017、2018 則用它在取出的腦裡活化輸出神經元（MBON），看 DAN 會不會跟著反應（見 [[t-mbon-dan-feedback]]）。優點是時間精確到毫秒，而且只動被標記的那幾顆 DAN。

它需要視黃醛（retinal）當輔因子，所以果蠅要先吃含全反式視黃醛的飼料、養在暗處。

**Chr2XXL** 是另一種**藍光**活化的通道（峰值約 460 nm），Tumkaya 2025 用它活化 DAN，把紅光留給 ORN，因此能在同一隻果蠅上分別控制兩條路徑。該篇指出它**關閉得慢**，而這個特性改變了實驗設計：獎賞制約沿用 12 次脈衝時做不出記憶，改成只給一次 3 秒的光才成功（見 [[s-tumkaya-2025-synthetic-memory-inception]]）。

**ChrimsonR** 是另一種紅光活化的通道，Handler 2019 只在閉迴路實驗用它（果蠅頭固定在顯微鏡下、腳踩泡沫球，球的轉動帶動送氣管，可同時看腦與行為）；Aso 2023 與 Yamada 2023 在電生理實驗用它活化 PAM 群。**Chrimson88** 是第三個版本，Aso 2023 與 Yamada 2023 用它（接 tdTomato 標籤）活化 MBON 或在多巴胺成像中活化 DAN。這幾個版本的差別本庫各篇都沒有說明：？待查。

**[[s-yamada-2023-second-order-conditioning]] 一篇裡就用了三個版本、三組光參數**：行為用 CsChrimson（627 nm、34.9 µW/mm²，LED 板在競技場底下），電生理用 ChrimsonR（625 nm、17 mW/mm²，經物鏡送到腦上，1 ms 脈衝 2 Hz × 120 下），離體多巴胺成像用 Chrimson88-tdTomato（660 nm、12 µW/mm²、1 秒）。跨實驗比較「活化強度」時要先看是哪一組。

## 版本與規模（光參數）

| 項目 | Hige 2015 | Handler 2019 |
|---|---|---|
| 通道 | CsChrimson（引 Klapoetke et al. 2014） | CsChrimson；閉迴路改用 ChrimsonR |
| 光源 | 627 nm LED，直接照在打開的腦上 | 行為小室：627 nm LED；閉迴路：565 nm，經顯微鏡物鏡照射 |
| 光強 | 14.7 mW/mm² | 小室約 18–40 μW/mm²；閉迴路約 150 μW/mm² |
| 生理實驗的光 | 1 ms × 4 下（2 Hz，氣味開始後 0.2 s 起）；單脈衝 1 ms × 1（氣味開始後 0.8 s）；長協定 1 ms × 120 下（2 Hz，配 60 s 氣味） | 離體腦不用光，改用 P2X2＋ATP；閉迴路 1 s 持續照光 |
| 行為實驗的光 | 500 ms × 12（從圖 7J 讀出，其他參數在補充資料：？待查） | 1 s 持續照光 |
| 視黃醛 | 電生理 0.5 mM、暗處 36–72 h；行為實驗在羽化（蛹變為成蟲）前 0.2 mM、之後 0.4 mM | 0.4 mM，1–3 日齡雌蠅轉入後暗養 2–3 天 |

數值出處見 [[numbers]]。**上表只列了兩篇**（欄位是「項目 × 來源」，加欄會讓表格過寬）；其餘各篇的光參數列在這裡，一篇一行：

- [[s-aso-2014-mbon-valence]]：20xUAS-CsChrimson-mVenus（attP18）；**617 nm**、照光區 34 µW/mm²，交界 10 mm 內由 34 降到 3 µW/mm²；協定分四段各 30 秒（照光兩段）。視黃醛羽化前 0.2 mM、之後 0.4 mM。作者只呈現 20xUAS 版本，並說 5x 與 10x 的初步結果顯示「表現太弱或太強都可能看不到表型」。
- [[s-aso-2019-nitric-oxide-cotransmitter]]：20×UAS-CsChrimson-mVenus；行為 627 nm、34.9 µW/mm²，1 分鐘氣味內給 30 下 1 秒光；離體鈣成像改用 660 nm，PPL1-γ1pedc→MBON 用 5 次、最高 1.2 mW/mm²，PPL1-γ1pedc→PAM 用 9 次、0.89 mW/mm²，每次 1 秒。
- [[s-aso-2023-upwind-neurons]]：行為 627 nm、34.9 µW/mm²（訓練時 20 秒氣味中第 14 秒起給三下 1 秒光）；電生理用 Chrimson88-tdTomato，光刺激 10 ms；可塑性實驗用 ChrimsonR-mVenus（R58E02-LexA），1 ms、2 Hz、120 下配 60 秒氣味。
- [[s-yamada-2023-second-order-conditioning]]：見上一節的三組參數。
- [[s-pribbenow-2022-postsynaptic-plasticity]]：lexAop-CsChrimson-tdTomato（R58E02-LexA）；離體腦，2 秒紅光、間隔 4 秒，配對時與噴乙醯膽鹼同時開始、共 5 次；**波長與強度論文未寫（？待查）**，另加 U25ND25 減光片以降低基線活化。
- [[s-eschbach-2021-learned-innate-valence-integration]]（幼蟲）：MBON 活化篩選 660 nm、4 µW/mm²，第 30 與第 75 秒各 15 秒；人工懲罰訓練 629 nm、2.5 µW/mm²；成像中的訓練改用 660 nm 雷射約 480 µW/mm²；離體活化 KC 用 625 nm、3 秒 × 4 次。**對照幼蟲本身對紅光就有輕微的嫌惡反應。**

## 庫內誰用了它

| 來源 | 活化哪些 DAN（驅動品系） | 用它做什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **未使用。** 該篇沒有活化 DAN，直接把多巴胺滴進腦裡 | — |
| [[s-hige-2015-heterosynaptic-plasticity]] | PPL1-γ1pedc（MB320C）；多型 PPL1（MB099C；Hige 說四型、Aso 2016 說兩型，見 [[syn-contradictions]] 1.4）；多數 PPL1 加少數 PAM（TH-GAL4） | 一邊記錄 MBON，一邊讓氣味與 DAN 活化配對；另以光代替電擊訓練果蠅 |
| [[s-handler-2019-dopamine-receptor-timing]] | PAM（MB042B）、PPL（MB504B）；閉迴路用 MB042B 驅動 ChrimsonR | 自由行走果蠅的順向／逆向配對與時間差掃描；閉迴路中同時記錄 γ4 MBON 與行為 |
| [[s-aso-2016-dan-cell-type-rules]] | 六組品系（MB320C、MB099C、MB630B、MB043C、MB213B、MB315C＋MB109B），另以 VT045661-LexA 驅動 LexA 版 CsChrimson；行為：627 nm、34.9 µW/mm²，標準訓練 60 s 內 30 下、每下 1 s；視黃醛羽化前 0.2 mM、之後 0.4 mM | 競技場中代替電擊或糖訓練，比較各型 DAN 的學習規則 |
| [[s-felsenberg-2017-re-evaluation]] | **活化的是 MBON 不是 DAN**：V2 群（R71D08-LexA 等）、γ2α′1 MBON（R25D01-LexA、MB077C）；離體腦，630 nm、0.85 mW/mm²，40 Hz × 10 ms 共 500 ms（圖 4d 為 200 ms）；視黃醛 1 mM | 看活化 MBON 後 PPL1 或 PAM 的鈣反應（MBON → DAN 的功能連結） |
| [[s-felsenberg-2018-memory-extinction]] | **活化的是 MBON**：M4β′ 與 M6（VT1211-LexA）；離體腦，參數同 Felsenberg 2017（500 ms） | 活化後 γ5 的 PAM 末梢 ΔF/F0 約 +1.75（5 個腦），γ4 無反應 |
| [[s-tumkaya-2025-synthetic-memory-inception]] | **活化的是感覺神經元不是 DAN**：Orco-Gal4 的 ORN（另有 Or42b、Gr21a）。論文寫「Chrimson」，品系為 BDSC:55135（帶 mVenus 標籤）；視黃醛 0.5 mM、實驗前 2 天換飼料、全程暗養 | 以紅光代替氣味當 CS。紅光由微投影機照半條通道，形成明暗選擇；該篇的 DAN 改用藍光的 Chr2XXL，兩色互不干擾 |
| [[s-huang-2024-dopamine-memory-dynamics]] | **活化的是 MBON**：MBON-γ1pedc>α/β（MB085C／UAS-CsChrimson-tdT）；頭固定、腳踩小球的活果蠅；625 nm、25 µW/mm²，30 下、每下 0.5 s、0.5 Hz，訓練時 CS+ 與 CS− 期間都照；全反式視黃醛 400 µM 餵 3–5 天 | 訓練期間讓這顆 MBON 持續放電，使它對 PPL1-α3 的抑制性回饋降不下來：照光的實驗組 5 分鐘記憶正常、3 小時記憶消失；照光的對照組（MB085C/+）與兩個不照光組 3 小時都正常（2 × 2 四組，每組 12 隻） |
| [[s-aso-2014-mbon-valence]] | **活化的是 MBON 不是 DAN**：25 條 split-GAL4 品系（覆蓋 22 型 MBON 中的 20 型）；另活化 CO₂ 受器（Gr63a）、苦味受器（Gr66a）與嗅葉投射神經元（NP225）當對照 | 未訓練、無氣味的光偏好篩檢：約 20 隻雌蠅在直徑 10 cm 的四象限場地裡，看牠們聚向或躲開照光的兩個象限；另做明暗交界的單隻軌跡分析。25 條中 9 條顯著（走開 3、靠近 6） |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | 七組驅動品系：PPL1 四型合一、PPL1-γ1pedc（MB320C）、PPL1-γ2α′1、PPL1-α3、PAM 群、PAM-γ5／β′2a、PAM-β′1；另以 Gr66a-GAL4 活化苦味感覺神經元 | 以紅光代替電擊或糖寫入記憶，並在 TH 突變背景（細胞照常放電、但做不出多巴胺）下重做，測價性反轉；離體鈣成像中活化 PPL1-γ1pedc，看 MBON 與其他 DAN 的反應 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | PAM 群（R58E02-LexA），只寫「a subset of DANs (PAM neurons)」、未列型別或顆數 | 離體腦＋TTX 中以紅光取代糖，與噴在 M6 樹突上的乙醯膽鹼配對，測試**不經 KC** 能否誘發突觸後可塑性 |
| [[s-aso-2023-upwind-neurons]] | 四組獎賞 DAN（MB043C＝α1、MB213B＝β1β2、MB312C＝γ4、MB109B＋MB315C＝γ5β′2a）與糖受器神經元（Gr64f split-GAL4）；另以 Chrimson88 活化 MBON（MB082C、MB310C、G0239-GAL4）、以 ChrimsonR 活化 PAM 群（R58E02-LexA） | 代替糖寫入區室專一的記憶；約 63 條品系的迎風活化篩選；電生理與鈣成像中活化上游 MBON |
| [[s-yamada-2023-second-order-conditioning]] | 行為：各型 PAM 的 split-GAL4（MB043C、MB109B＋MB315C、MB213B、MB312C、MB032B、MB196B）與糖受器神經元 Gr64f-GAL4；中間神經元 SMP108（SS67221、SS45234）、SMP353/354（SS33917）。電生理與成像：R58E02-LexA、MB043-split-LexA | 以光代替糖寫下一階記憶，再測它能不能教出二階記憶；光活化 SMP108 當增強訊號；離體以多巴胺感測器 DA2m 看活化 SMP108 時各區室收到多少多巴胺 |
| [[s-eschbach-2021-learned-innate-valence-integration]] | **幼蟲，而且活化的不是 DAN**：Basin（GMR72F11，當人工懲罰）、各型 MBON（18 型）、CN-33、全部 KC（GMR14H06-LexA）、ORN42b | 以人工懲罰配天生喜歡的氣味做訓練；逐型活化 MBON 判定它推動靠近還是走開；看匯聚神經元活化後的行為效果，以及 KC→匯聚神經元的功能連結（離體加 PTX／MCA 拆開興奮與抑制） |

## 已知的問題

- **光強不能跨篇直接比。** Hige 的 14.7 mW/mm² 照在打開的腦上，Handler 的 18–40 μW/mm² 照在小盒裡自由行走的果蠅身上：一個以毫瓦（mW）、一個以微瓦（μW）為單位，光要穿過的組織也不同，到達 DAN 的實際光量無從比較。
- **同一篇裡，生理與行為的光協定也不同。** Hige 生理用 1 ms 短脈衝、行為用 500 ms × 12，所以「突觸變弱」與「行為學到」是在兩種刺激下分別看到的。
- **「光照有效」靠補充資料。** Hige 2015 說光脈衝能讓 PPL1-γ1pedc 與 PPL1-α′2α2 可靠放電，證據在補充圖 S2：？待查。Hige 2015 比較了兩個區室的誘發門檻（要多少次「氣味＋光」配對才會讓突觸變弱）：γ1pedc 用 MB320C（一顆 DAN），α2 用 MB099C（多型 DAN）。不同品系每次光照放出的多巴胺可能不同，所以門檻差異可能部分來自活化強度，是這項比較的混淆因子（見 [[e-mb099c]]、[[e-mushroom-body]]）。
- **光本身的作用要排除。** Handler 2019 的行為指標是「訓練後果蠅往氣味源走的距離比訓練前多幾 mm」。只帶 CsChrimson、沒有 DAN 驅動品系（所以光照不會活化 DAN）的對照組，在 DAN 晚氣味 1 s 的時序下也多走了約 0.7 mm（見 [[numbers]]），表示光與流程本身就有小幅效果；光照單獨的對照在補充圖 S1D–E：？待查。
- **「活化 MBON 讓 DAN 有反應」只說明功能上相連。** Felsenberg 2017、2018 的離體實驗沒有氣味、n 小（4–5），不能區分直接突觸與間接路徑；Felsenberg 2018 的 VT1211 同時標 M4β′ 與 M6，分不出是哪一顆在驅動 γ5。
- **Huang 2024 的活化不是代替懲罰，而是「壓住可塑性的後果」。** 它照的是 MBON，目的是抵消訓練讓這顆 MBON 對 CS+ 變弱的效果；結果只測了 3 小時一個長時間點，行為只在小球上測。
- **Cohn 2015 也提到一種「紅移的 channelrhodopsin」**（補充圖 S6A），論文沒寫是哪一種，本頁不把它算成 CsChrimson。
- **同一篇裡換通道版本，就換了一套光參數。** [[s-yamada-2023-second-order-conditioning]] 的行為、電生理、成像分別用 CsChrimson、ChrimsonR、Chrimson88，波長 627／625／660 nm、強度 34.9 µW/mm²／17 mW/mm²／12 µW/mm²（相差三個數量級）。[[s-aso-2023-upwind-neurons]] 也是三種通道混用。「某型 DAN 被活化了多少」在這些篇裡無法跨實驗比較。
- **活化的不一定是 DAN，也不一定是成蟲。** 本頁表中有五篇活化的是 MBON 或感覺神經元：Aso 2014b（MBON 篩檢）、Felsenberg 2017／2018（MBON→DAN）、Huang 2024（MBON）、Aso 2023（MBON 與糖受器神經元）、Eschbach 2021（幼蟲的 Basin、MBON、KC、ORN）。引用「光遺傳活化」時要先看活化的是哪一類細胞。
- **幼蟲的對照本身就怕紅光。** [[s-eschbach-2021-learned-innate-valence-integration]] 的空白品系對照（Nexp＝343、超過 10,000 隻幼蟲）對紅光有輕微的嫌惡反應，所以 MBON 活化的效果是疊在這個背景上判讀的。
- **光參數有時候根本沒寫。** [[s-pribbenow-2022-postsynaptic-plasticity]] 的離體實驗沒有給波長與強度（？待查），只說加了 U25ND25 減光片以降低基線活化——也就是作者知道這個通道在成像用的雷射下會被意外打開。

## 相關

- 細胞：[[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-kenyon-cell]]；品系：[[e-split-gal4]]、[[e-r58e02]]
- 其他操作工具：[[e-dtrpa1]]、[[e-shibire-ts]]、[[e-tnt]]、[[e-p2x2]]
- 概念：[[c-us-substitution]]、[[c-cs-us-timing]]、[[c-performance-index]]、[[c-mb-compartment]]、[[c-ex-vivo-explant]]
- 主題：[[t-timing-rules]]、[[t-mbon-dan-feedback]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-tumkaya-2025-synthetic-memory-inception]]、[[s-aso-2014-mbon-valence]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-aso-2023-upwind-neurons]]、[[s-yamada-2023-second-order-conditioning]]、[[s-eschbach-2021-learned-innate-valence-integration]]
