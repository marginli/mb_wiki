---
title: 多巴胺神經元（dopaminergic neuron, DAN）
created: 2026-10-25
updated: 2026-11-13
tags: [entity, active, mb-learning]
confidence: medium
---

# 多巴胺神經元（dopaminergic neuron, DAN）

## 是什麼

釋放多巴胺（dopamine）的神經元。在蕈狀體學習的模型裡，DAN 把「剛剛發生了壞事或好事」送進 [[e-mushroom-body]]：它的軸突末梢伸到 [[e-kenyon-cell]]（KC）與 [[e-mbon]]（MBON）之間的突觸旁，每一型 DAN 只支配葉上的一個或幾個區室（[[c-mb-compartment]]）。DAN 也不只是被動轉播外界的獎懲：Ichinose 2015、Cohn 2015、Felsenberg 2017、2018、Huang 2024 都顯示輸出神經元（MBON）會回頭影響 DAN 的活動（見 [[t-mbon-dan-feedback]]）。

本庫各篇提到兩群與蕈狀體有關的 DAN（以細胞體所在的位置命名的細胞群）：

| 細胞群 | 來源怎麼描述 |
|---|---|
| **PPL1**（Hige 2015、Aso 2016、Felsenberg 2017／2018 的寫法）／**PPL**（Handler 2019 的寫法） | 傳遞懲罰。傳統的學習實驗用電擊當懲罰；Hige 2015 引文獻說，熱遺傳（讓神經元帶溫度敏感通道、升溫使其放電）活化 PPL1-γ1pedc 可取代電擊；Handler 2019 說 PPL 足以驅動嫌惡記憶。Felsenberg 2017：主要支配垂直的 α、α′ 葉，另有水平 γ 葉根部的 γ1、γ2；支配 MB 的 PPL1 共六型（延伸圖 6b）。Felsenberg 2018 的說法是 PPL1 裡「有許多」送懲罰訊號。Huang 2024 以電壓成像量五型 PPL1 的放電：電擊讓 γ1pedc、γ2α′1、α3 增加，吃糖讓 γ1pedc、γ2α′1、α′2α2、α3 減少，氣味依果蠅喜不喜歡而增加或減少——**雙向**，不只報告懲罰。Mao 2009（最早的一篇）：PPL1 共 12 顆、八種投射樣式，其中五型伸進葉（α 尖端、α′ 尖端、上段、下段與交界、腳跟與柄末端），並把後三型對到舊名 MB-V1、MB-MV1、MB-MP1。Aso 2014a 以 split-GAL4 列出支配葉的六型（γ1pedc、γ1、γ2α′1、α′3、α′2α2、α3），其中 PPL1-γ1 只在 TH-GAL4 的隨機標記中看過、做不出品系 |
| **PAM** | Handler 2019：多報告獎賞。Hige 2015 只在 TH-GAL4 的圖說中提到「少數 PAM DAN」，沒有說明功能。Aso 2016 把 PAM 各型歸在獎賞（圖 2A）；Felsenberg 2017：支配水平的 β、β′、γ 葉（另有 α1）；Felsenberg 2018：PAM 裡「有許多」送獎賞訊號，而消退（[[c-memory-extinction]]）需要它；Ichinose 2015：PAM-α1 傳遞長期記憶所需的獎賞（[[e-pam-alpha1]]）。Mao 2009：抗 TH 染色約 100 顆／半腦，但 TH-GAL4 只標到約 13 顆，所以該篇幾乎沒有量到水平葉的多巴胺功能。Aso 2014a 以 split-GAL4 分出 14 型、98 顆。Pribbenow 2022 只以「PAM neurons（R58E02-LexA）」稱呼，不列型別 |

※ 推論：PPL1 與 PPL 指同一群。依據：兩篇都把它描述為傳遞懲罰的 DAN 群；兩篇的驅動品系都用到 TH（合成多巴胺的酵素酪胺酸羥化酶）的調控序列；而且 Handler 2019 的「PPL」品系 MB504B，Felsenberg 2017 也用、並說它標四型 PPL1（[[e-mb504b]]）。這讓兩個名稱指向同一批細胞的可能性提高，但沒有一篇明說兩個名稱的關係（[[syn-contradictions]] 4.4 部分解決）。

## 庫內誰用了它

| 來源 | 怎麼讓多巴胺出現 | 用到的 DAN 與驅動品系 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **沒有活化 DAN。** 直接把多巴胺加進灌流液（浴灌，10 nM–10 mM），或用玻璃細管噴在垂直葉（細管內 1 mM） | 無。只引 Mao & Davis 2009 說明多巴胺神經元支配蕈狀體 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 光遺傳：DAN 表現 [[e-cschrimson]]，紅光一照就放電 | **PPL1-γ1pedc**（舊名 MB-MP1），由 MB320C 標記，只標這一顆；**MB099C** 依 Hige 2015 標四型 PPL1（γ2α′1、α′2α2、α′3、α3），依 Aso 2016 只標 γ2α′1 與 α′2α2 兩型（[[e-mb099c]]、[[syn-contradictions]] 1.4），兩篇都說不標 PPL1-γ1pedc；**TH-GAL4** 標多數 PPL1（含 γ1pedc）、少數 PAM 與蕈狀體以外的許多 DAN，當正對照（已知應該有效的組，用來確認方法本身有用） |
| [[s-handler-2019-dopamine-receptor-timing]] | 行為：光遺傳（CsChrimson；閉迴路實驗用 ChrimsonR。閉迴路＝果蠅頭固定在顯微鏡下、腳踩泡沫球，球的轉動帶動送氣管，可同時看腦與行為）；離體腦：化學遺傳，DAN 表現 ATP 門控通道 P2X2，滴 ATP 使其放電；另有一組用真的電擊（補充圖 S3E：？待查） | **PAM**：MB042B（行為、閉迴路）、R58E02-LexA（離體；基因型表標為「γ4–5 DANs」，但 Felsenberg 2017 說同一品系標 13 型 PAM，見 [[e-r58e02]]、[[syn-contradictions]] 1.5）；**PPL**：MB504B（行為，論文說它支配六個區室，沒列出是哪六個）；γ2 DAN：73F07-LexA（補充圖 S3D）；TH-Gal4 加 DDC-Gal4 用來在 DAN 表現 VMAT-pHluorin（見下段） |
| [[s-cohn-2015-coordinated-neuromodulation]] | 化學遺傳：P2X2＋ATP（[[e-p2x2]]）活化 58E02 標記的 DAN（含 γ4、γ5，γ3 不穩定）或 γ2 DAN；另量 DAN 本身：TH 與 DDC 啟動子讓各格 DAN 末梢表現只在突觸前發光的 sytGCaMP | 吃糖時 γ4/γ5 DAN 興奮、γ2/γ3 被抑制，電擊相反；固定果蠅掙扎時像電擊、靜止時像吃糖；活化任一格 γ MBON 都改變各格 DAN |
| [[s-aso-2016-dan-cell-type-rules]] | 光遺傳（CsChrimson），六組驅動品系各活化一或兩型 DAN | PPL1-γ1pedc（MB320C）、PPL1-γ2α′1＋α′2α2（MB099C）、PPL1-α3（MB630B，新做）、PAM-α1（MB043C）、β1/β2 的 PAM（MB213B）、γ5/β′2a 的 PAM（MB315C＋MB109B）；R58E02-GAL4 約 90 顆 PAM |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 以 shibire^ts 阻斷（[[e-shibire-ts]]）、RNAi 降低 NMDA 受體 | PAM-α1（MB299B；雙標記用 R72D01-LexA） |
| [[s-felsenberg-2017-re-evaluation]] | **阻斷而非活化**：shibire^ts 在記憶再活化期間關掉 DAN；離體量 DAN 對 MBON 活化的鈣反應 | TH-GAL4（全部六型 PPL1）、MB504B（四型 PPL1）、R58E02（13 型 PAM）、MB296B／R73F07（PPL1-γ2α′1）等 |
| [[s-felsenberg-2018-memory-extinction]] | 阻斷：shibire^ts；離體成像 PAM 末梢 | R58E02-GAL4（PAM，阻斷後消退消失）、MB504B（PPL1，阻斷後消退照常）；R48B04-GAL4 成像 γ4、γ5、β′2p、β′2m 的 PAM |
| [[s-tumkaya-2025-synthetic-memory-inception]] | 光遺傳：DAN 表現**藍光**活化的 Chr2XXL，把紅光讓給 ORN（見 [[e-cschrimson]]） | **TH-LexA**，自述為「含 PPL1 在內的 TH⁺ 子集」，未列型別（見 [[e-th-gal4]]）；**R58E02-LexA**，只寫「PAM」，未列型別（見 [[e-r58e02]]）。兩個品系的涵蓋範圍本篇都沒有交代，免疫染色也分辨不出來（anti-ChR2 同時認兩種通道蛋白） |
| [[s-huang-2024-dopamine-memory-dynamics]] | **沒有人工活化 DAN。** 以電壓成像（指示劑 pAce，每秒 1,000 張）量 DAN 對真的電擊（20 V、0.2 s）、糖與氣味的自然放電；另在 PPL1-α3 以 RNAi 降低 GABA-A 受體 RDL 與麩胺酸門控氯通道 GluCl-α，檢查 MBON 回饋 | 只量 **PPL1** 五型（γ1pedc、γ2α′1、α′2α2、α3、α′3），沒有量 PAM。品系：MB504B（圖 1b 同時標 γ1pedc、γ2α′1、α′2α2）、TH-LexA；鈣成像對照用 R82C10-LexA（PPL1-α′2α2）與 MB065B（PPL1-α3）。各型電壓成像的品系對照在延伸表 1，未印出（？待查） |
| [[s-mao-2009-dopaminergic-neuron-types]] | **沒有人工活化 DAN。** TH-GAL4 > UAS-G-CaMP 量 DAN 末梢對真的電擊（定電流 0.0001–0.1 mA）與氣味（MCH、OCT）的鈣反應；另以 flip-out 單細胞選殖描繪形態 | TH-GAL4（整群）。解剖上分出三群伸進蕈狀體：PAM（抗 TH 約 100 顆，TH-GAL4 只標到約 13 顆）、PPL1（12 顆，五型進葉）、PPL2ab（進萼部）。功能只量 PPL1 支配的垂直葉各段 |
| [[s-burke-2012-octopamine-dopamine-reward]] | 熱遺傳活化（uas-dTrpA1，31 °C）代替糖，或以 shibire^ts 阻斷；另以 RNAi 在指定 DAN 中降低章魚胺受體 | **PAM**：0273-GAL4（與抗 TH 共染判定，標到全部約 130 顆 PAM）、0104-GAL4（約 40 顆）；**PPL1**：c061-GAL4;MBGAL80 標 MB-MP1（即 PPL1-γ1pedc），只用於阻斷與 RNAi |
| [[s-aso-2014-mb-architecture]] | **不操弄、不量活性**，純解剖 | 支配葉的 20 型：PAM 14 型、PPL1 6 型；另有支配萼部的 PPL2ab。PPL1 每型 1–2 顆、PAM 每型最多約 20 顆；PAM 的總數有三套（split-GAL4 標到 98 顆、抗多巴胺染色估 115–135 顆、逐格 PA-GFP 相加約 154 顆，作者自陳最後一個是高估） |
| [[s-aso-2014-mbon-valence]] | 熱遺傳（dTrpA1）活化代替電擊；shibire^ts 阻斷 | PPL1-γ1pedc（MB438B，依表 2 另弱標 PPL1-α2α′2）；雙標記用 MB320C。其餘 DAN 只在圖 1A 引文獻整理 |
| [[s-dylla-2017-trace-conditioning-dan-plasticity]] | **沒有人工活化 DAN。** 以 GCaMP3 量 DAN 對真的電擊與氣味的反應，比較配對與不配對訓練 | TH-GAL4：γ1 有 PPL1-γ1pedc 與 PPL1-γ1、γ2/α′1 有 PPL1-γ2α′1；PAM 只標到 12 顆。另量扇形體、橢圓體的 DAN 當對照 |
| [[s-aso-2019-nitric-oxide-cotransmitter]] | CsChrimson 紅光活化（627 nm、34.9 µW/mm²，1 分鐘氣味內給 30 下 1 秒光）代替電擊或糖；另以 Gr66a-GAL4 活化苦味感覺神經元間接活化 PPL1。**關鍵操作是在 TH 突變背景下活化 DAN：細胞照常放電，但沒有多巴胺可放** | 七個驅動品系：PPL1 四型合一、PPL1-γ1pedc（MB320C）、PPL1-γ2α′1、PPL1-α3、PAM 群、PAM-γ5／β′2a、PAM-β′1 |
| [[s-pribbenow-2022-postsynaptic-plasticity]] | 離體腦中以 CsChrimson 紅光活化 PAM 群代替糖，與噴在 MBON 樹突上的乙醯膽鹼配對（全程在 TTX 下）；活體 FRAP 則直接注射多巴胺 10 mM | R58E02-LexA，只寫「一部分 DAN（PAM 神經元）」，沒有列型別或顆數 |
| [[s-aso-2023-upwind-neurons]] | CsChrimson／ChrimsonR 光活化代替糖 | PAM-α1（MB043C）、β1β2（MB213B）、γ4（MB312C）、γ5β′2a（MB109B＋MB315C）；量 UpWiN 可塑性時用 R58E02-LexA（標到多型 PAM，作者自陳 β1 可能有貢獻） |
| [[s-yamada-2023-second-order-conditioning]] | 光遺傳（CsChrimson／ChrimsonR／Chrimson88，627 或 660 nm）活化各型 PAM 代替糖；TNT 阻斷；另以 DA2m 在離體腦量各區室實際收到的多巴胺 | **只做 PAM 群**：MB043C（PAM-α1，標到 5 顆／該型共 7 顆）、MB109B＋MB315C（γ5、β′2a，16／30）、MB213B（β1、β2，12／22）、MB312C（γ4，11／23）、MB032B（β′2m）、MB196B（γ4、γ4<γ1γ2、γ5、β′2a，約 27 顆）、R58E02-LexA。PPL1 完全沒有量 |

品系的專一性問題見 [[e-split-gal4]]。

**Handler 2019 也量了 DAN 本身。** 用 GCaMP6s（DAN 的鈣，約等於放電活動）、VMAT-pHluorin（多巴胺的釋放）與 KC 軸突上的 GRAB_DA1m（KC 收到的多巴胺），發現順向配對（氣味或 KC 刺激在前、DAN 在後）與逆向配對（DAN 在前）時三者都一樣（樣本數見 [[numbers]]）。所以先後次序不是靠「送來多少多巴胺」區分，而是靠 KC 怎麼讀（見 [[c-camp-signaling]]）。

## 已知的問題

- **PPL 與 PAM 的時間規則在 Handler 2019 的行為資料裡不一樣。** Handler 把「DAN 比氣味晚幾秒」從負（DAN 在前）掃到正（DAN 在後），量果蠅之後追氣味的變化。PPL 與 PAM 都會在某個時間差上把效果翻成反方向，但翻轉的位置不同：PPL 約在 DAN 晚 0.49 s、PAM 約在 DAN 早 0.44 s，相差約 0.9 s（以相鄰兩點線性內插，本庫推算，見 [[numbers]]）。0 秒落在 PPL 翻轉點（+0.49 s）之前、PAM 翻轉點（−0.44 s）之後，所以氣味與 DAN 同時開始時，PPL 給的效果和它的逆向配對同方向，PAM 給的效果卻和它的順向配對同方向。至於 PPL 的翻轉點為何不同，論文沒有分子層次的檢驗：離體腦中的 cAMP 等分子實驗只做了 PAM 對 γ4 區室（見 [[t-timing-rules]]）。
- **Hige 2015 只活化 PPL1**（TH-GAL4 那組另含少數 PAM），只看到突觸變弱；獎賞 DAN 會讓突觸往哪個方向變，該篇沒有測。
- **「活化 DAN」不等於「真的懲罰或獎賞」。** 光遺傳與 ATP 都是人工刺激，見 [[c-us-substitution]]。Tomchik 2009 更是連 DAN 都沒動，直接把多巴胺加進灌流液；灌入的濃度也不等於組織內的實際濃度。
- **品系涵蓋的範圍沒有完整列出**：MB504B 的六個區室、MB042B 涵蓋哪些區室，Handler 2019 都沒列出；行為結果因此可能來自 γ4 以外的區室。
- **同一品系，各篇寫的涵蓋範圍不同。** MB099C（[[syn-contradictions]] 1.4）與 R58E02（1.5）都有兩種說法，本頁不裁決。
- **阻斷只說明「必要」。** Felsenberg 2017、2018 與 Ichinose 2015 用溫度阻斷證明某群 DAN 在某段時間不可缺，不說明它們在正常果蠅裡被什麼驅動；Felsenberg 2018 想在活體看 γ5 DAN 對氣味的反應，因自發振盪太強沒量到（data not shown）。
- **DAN 末梢的鈣不等於多巴胺釋放。** Cohn 2015 以 sytGCaMP 的末梢鈣代替釋放量，沒有直接量多巴胺。Huang 2024 量的是放電，同樣沒有量多巴胺釋放（作者列為未來方向）。
- **鈣成像看不到 DAN 放電「減少」。** Huang 2024 延伸圖 13：同一型 PPL1-α3，電壓成像看到吸引氣味讓放電明顯下降，鈣成像（jGCaMP7b）幾乎看不出來；強刺激時鈣指示劑又會飽和，低估「氣味＋電擊」的相加。所以 Cohn 2015、Felsenberg 2018 等用鈣成像量 DAN 的結果，「沒看到下降」不能讀成「沒有下降」。
- **支配蕈狀體的 PPL1 是五型還是六型，各篇說法不同。** Mao 2009 找到五型進葉、自承可能有漏；[[s-aso-2014-mb-architecture]] 表 1 列六型，但第六型 PPL1-γ1 只在 TH-GAL4 的隨機標記中看過（表 1 註腳），做不出 split-GAL4；Felsenberg 2017 延伸圖 6b 寫六型；Huang 2024 量得到的是五型。差別來自工具，不是細胞數不同（見 [[syn-contradictions]]）。
- **多巴胺神經元不只放多巴胺。** [[s-aso-2019-nitric-oxide-cotransmitter]] 在 TH 突變背景下活化 DAN（有活動、沒有多巴胺），PPL1-γ1pedc 與 PAM-γ5／β′2a 造出的記憶**價性相反**，並指認一氧化氮是這兩型的共同傳遞物；PPL1-γ2α′1 則不反轉，表示它的共同傳遞物與多巴胺同號。所以「活化某型 DAN」不等於「在那一格給多巴胺」。
- **PAM 的細胞數在庫內有幾個數字，定義不同。** Burke 2012 的「約 130」是與抗 TH 共染判定的 PAM 全群，Mao 2009 的抗 TH 計數約 100、TH-GAL4 只標約 13，Aso 2014a 的 split-GAL4 標到 98 顆（同篇另列抗多巴胺 115–135、PA-GFP 相加約 154，後者作者自陳高估），Aso 2016 的「約 90」是 R58E02-GAL4 所標的數目。見 [[numbers]]，不是矛盾。
- **用鈣成像得到的否定結果要留餘地。** [[s-dylla-2017-trace-conditioning-dan-plasticity]] 以 GCaMP3 量 DAN，結論是 DAN 的變化不符合預測誤差；但它量的是鈣，而 Huang 2024 延伸圖 13 示範了鈣成像看不到 DAN 放電下降（見下一條）。
- **Huang 2024 的放電率是在弱電擊下量的。** 20 V、每下 0.2 s，T 迷宮慣用 60–90 V、1.25 s；不能直接當成 T 迷宮條件下 DAN 的放電率。

## 相關

- 結構與細胞：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-mbon]]
- 工具：[[e-split-gal4]]、[[e-cschrimson]]、[[e-gcamp]]、[[e-p2x2]]、[[e-shibire-ts]]
- 細胞型與品系：[[e-ppl1-gamma1pedc]]、[[e-ppl1-gamma2alpha1]]、[[e-ppl1-alpha2alpha2]]、[[e-ppl1-alpha3]]、[[e-pam-alpha1]]、[[e-mb099c]]、[[e-mb504b]]、[[e-r58e02]]、[[e-th-gal4]]
- 概念：[[c-us-substitution]]、[[c-cs-us-timing]]、[[c-mb-compartment]]、[[c-camp-signaling]]
- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]；矛盾：[[syn-contradictions]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-huang-2024-dopamine-memory-dynamics]]、[[s-mao-2009-dopaminergic-neuron-types]]、[[s-burke-2012-octopamine-dopamine-reward]]、[[s-aso-2014-mb-architecture]]、[[s-aso-2014-mbon-valence]]、[[s-dylla-2017-trace-conditioning-dan-plasticity]]、[[s-aso-2019-nitric-oxide-cotransmitter]]、[[s-pribbenow-2022-postsynaptic-plasticity]]、[[s-aso-2023-upwind-neurons]]、[[s-yamada-2023-second-order-conditioning]]
