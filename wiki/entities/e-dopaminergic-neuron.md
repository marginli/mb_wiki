---
title: 多巴胺神經元（dopaminergic neuron, DAN）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# 多巴胺神經元（dopaminergic neuron, DAN）

## 是什麼

釋放多巴胺（dopamine）的神經元。在蘑菇體學習的模型裡，DAN 把「剛剛發生了壞事或好事」送進 [[e-mushroom-body]]：它的軸突末梢伸到 [[e-kenyon-cell]]（KC）與 [[e-mbon]]（MBON）之間的突觸旁，每一型 DAN 只支配葉上的一個或幾個區室（[[c-mb-compartment]]）。DAN 也不只是被動轉播外界的獎懲：Ichinose 2015、Cohn 2015、Felsenberg 2017、2018 都顯示輸出神經元（MBON）會回頭影響 DAN 的活動（見 [[t-mbon-dan-feedback]]）。

本庫各篇提到兩群與蘑菇體有關的 DAN（以細胞體所在的位置命名的細胞群）：

| 細胞群 | 來源怎麼描述 |
|---|---|
| **PPL1**（Hige 2015、Aso 2016、Felsenberg 2017／2018 的寫法）／**PPL**（Handler 2019 的寫法） | 傳遞懲罰。傳統的學習實驗用電擊當懲罰；Hige 2015 引文獻說，熱遺傳（讓神經元帶溫度敏感通道、升溫使其放電）活化 PPL1-γ1pedc 可取代電擊；Handler 2019 說 PPL 足以驅動嫌惡記憶。Felsenberg 2017：主要支配垂直的 α、α′ 葉，另有水平 γ 葉根部的 γ1、γ2；支配 MB 的 PPL1 共六型（延伸圖 6b）。Felsenberg 2018 的說法是 PPL1 裡「有許多」送懲罰訊號 |
| **PAM** | Handler 2019：多報告獎賞。Hige 2015 只在 TH-GAL4 的圖說中提到「少數 PAM DAN」，沒有說明功能。Aso 2016 把 PAM 各型歸在獎賞（圖 2A）；Felsenberg 2017：支配水平的 β、β′、γ 葉（另有 α1）；Felsenberg 2018：PAM 裡「有許多」送獎賞訊號，而消退（[[c-memory-extinction]]）需要它；Ichinose 2015：PAM-α1 傳遞長期記憶所需的獎賞（[[e-pam-alpha1]]） |

※ 推論：PPL1 與 PPL 指同一群。依據：兩篇都把它描述為傳遞懲罰的 DAN 群；兩篇的驅動品系都用到 TH（合成多巴胺的酵素酪胺酸羥化酶）的調控序列；而且 Handler 2019 的「PPL」品系 MB504B，Felsenberg 2017 也用、並說它標四型 PPL1（[[e-mb504b]]）。這讓兩個名稱指向同一批細胞的可能性提高，但沒有一篇明說兩個名稱的關係（[[syn-contradictions]] 4.4 部分解決）。

## 庫內誰用了它

| 來源 | 怎麼讓多巴胺出現 | 用到的 DAN 與驅動品系 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **沒有活化 DAN。** 直接把多巴胺加進灌流液（浴灌，10 nM–10 mM），或用玻璃細管噴在垂直葉（細管內 1 mM） | 無。只引 Mao & Davis 2009 說明多巴胺神經元支配蘑菇體 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 光遺傳：DAN 表現 [[e-cschrimson]]，紅光一照就放電 | **PPL1-γ1pedc**（舊名 MB-MP1），由 MB320C 標記，只標這一顆；**MB099C** 依 Hige 2015 標四型 PPL1（γ2α′1、α′2α2、α′3、α3），依 Aso 2016 只標 γ2α′1 與 α′2α2 兩型（[[e-mb099c]]、[[syn-contradictions]] 1.4），兩篇都說不標 PPL1-γ1pedc；**TH-GAL4** 標多數 PPL1（含 γ1pedc）、少數 PAM 與蘑菇體以外的許多 DAN，當正對照（已知應該有效的組，用來確認方法本身有用） |
| [[s-handler-2019-dopamine-receptor-timing]] | 行為：光遺傳（CsChrimson；閉迴路實驗用 ChrimsonR。閉迴路＝果蠅頭固定在顯微鏡下、腳踩泡沫球，球的轉動帶動送氣管，可同時看腦與行為）；離體腦：化學遺傳，DAN 表現 ATP 門控通道 P2X2，滴 ATP 使其放電；另有一組用真的電擊（補充圖 S3E：？待查） | **PAM**：MB042B（行為、閉迴路）、R58E02-LexA（離體；基因型表標為「γ4–5 DANs」，但 Felsenberg 2017 說同一品系標 13 型 PAM，見 [[e-r58e02]]、[[syn-contradictions]] 1.5）；**PPL**：MB504B（行為，論文說它支配六個區室，沒列出是哪六個）；γ2 DAN：73F07-LexA（補充圖 S3D）；TH-Gal4 加 DDC-Gal4 用來在 DAN 表現 VMAT-pHluorin（見下段） |
| [[s-cohn-2015-coordinated-neuromodulation]] | 化學遺傳：P2X2＋ATP（[[e-p2x2]]）活化 58E02 標記的 DAN（含 γ4、γ5，γ3 不穩定）或 γ2 DAN；另量 DAN 本身：TH 與 DDC 啟動子讓各格 DAN 末梢表現只在突觸前發光的 sytGCaMP | 吃糖時 γ4/γ5 DAN 興奮、γ2/γ3 被抑制，電擊相反；固定果蠅掙扎時像電擊、靜止時像吃糖；活化任一格 γ MBON 都改變各格 DAN |
| [[s-aso-2016-dan-cell-type-rules]] | 光遺傳（CsChrimson），六組驅動品系各活化一或兩型 DAN | PPL1-γ1pedc（MB320C）、PPL1-γ2α′1＋α′2α2（MB099C）、PPL1-α3（MB630B，新做）、PAM-α1（MB043C）、β1/β2 的 PAM（MB213B）、γ5/β′2a 的 PAM（MB315C＋MB109B）；R58E02-GAL4 約 90 顆 PAM |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 以 shibire^ts 阻斷（[[e-shibire-ts]]）、RNAi 降低 NMDA 受體 | PAM-α1（MB299B；雙標記用 R72D01-LexA） |
| [[s-felsenberg-2017-re-evaluation]] | **阻斷而非活化**：shibire^ts 在記憶再活化期間關掉 DAN；離體量 DAN 對 MBON 活化的鈣反應 | TH-GAL4（全部六型 PPL1）、MB504B（四型 PPL1）、R58E02（13 型 PAM）、MB296B／R73F07（PPL1-γ2α′1）等 |
| [[s-felsenberg-2018-memory-extinction]] | 阻斷：shibire^ts；離體成像 PAM 末梢 | R58E02-GAL4（PAM，阻斷後消退消失）、MB504B（PPL1，阻斷後消退照常）；R48B04-GAL4 成像 γ4、γ5、β′2p、β′2m 的 PAM |

品系的專一性問題見 [[e-split-gal4]]。

**Handler 2019 也量了 DAN 本身。** 用 GCaMP6s（DAN 的鈣，約等於放電活動）、VMAT-pHluorin（多巴胺的釋放）與 KC 軸突上的 GRAB_DA1m（KC 收到的多巴胺），發現順向配對（氣味或 KC 刺激在前、DAN 在後）與逆向配對（DAN 在前）時三者都一樣（樣本數見 [[numbers]]）。所以先後次序不是靠「送來多少多巴胺」區分，而是靠 KC 怎麼讀（見 [[c-camp-signaling]]）。

## 已知的問題

- **PPL 與 PAM 的時間規則在 Handler 2019 的行為資料裡不一樣。** Handler 把「DAN 比氣味晚幾秒」從負（DAN 在前）掃到正（DAN 在後），量果蠅之後追氣味的變化。PPL 與 PAM 都會在某個時間差上把效果翻成反方向，但翻轉的位置不同：PPL 約在 DAN 晚 0.49 s、PAM 約在 DAN 早 0.44 s，相差約 0.9 s（以相鄰兩點線性內插，本庫推算，見 [[numbers]]）。0 秒落在 PPL 翻轉點（+0.49 s）之前、PAM 翻轉點（−0.44 s）之後，所以氣味與 DAN 同時開始時，PPL 給的效果和它的逆向配對同方向，PAM 給的效果卻和它的順向配對同方向。至於 PPL 的翻轉點為何不同，論文沒有分子層次的檢驗：離體腦中的 cAMP 等分子實驗只做了 PAM 對 γ4 區室（見 [[t-timing-rules]]）。
- **Hige 2015 只活化 PPL1**（TH-GAL4 那組另含少數 PAM），只看到突觸變弱；獎賞 DAN 會讓突觸往哪個方向變，該篇沒有測。
- **「活化 DAN」不等於「真的懲罰或獎賞」。** 光遺傳與 ATP 都是人工刺激，見 [[c-us-substitution]]。Tomchik 2009 更是連 DAN 都沒動，直接把多巴胺加進灌流液；灌入的濃度也不等於組織內的實際濃度。
- **品系涵蓋的範圍沒有完整列出**：MB504B 的六個區室、MB042B 涵蓋哪些區室，Handler 2019 都沒列出；行為結果因此可能來自 γ4 以外的區室。
- **同一品系，各篇寫的涵蓋範圍不同。** MB099C（[[syn-contradictions]] 1.4）與 R58E02（1.5）都有兩種說法，本頁不裁決。
- **阻斷只說明「必要」。** Felsenberg 2017、2018 與 Ichinose 2015 用溫度阻斷證明某群 DAN 在某段時間不可缺，不說明它們在正常果蠅裡被什麼驅動；Felsenberg 2018 想在活體看 γ5 DAN 對氣味的反應，因自發振盪太強沒量到（data not shown）。
- **DAN 末梢的鈣不等於多巴胺釋放。** Cohn 2015 以 sytGCaMP 的末梢鈣代替釋放量，沒有直接量多巴胺。

## 相關

- 結構與細胞：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-mbon]]
- 工具：[[e-split-gal4]]、[[e-cschrimson]]、[[e-gcamp]]、[[e-p2x2]]、[[e-shibire-ts]]
- 細胞型與品系：[[e-ppl1-gamma1pedc]]、[[e-ppl1-gamma2alpha1]]、[[e-pam-alpha1]]、[[e-mb099c]]、[[e-mb504b]]、[[e-r58e02]]、[[e-th-gal4]]
- 概念：[[c-us-substitution]]、[[c-cs-us-timing]]、[[c-mb-compartment]]、[[c-camp-signaling]]
- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]、[[t-mbon-dan-feedback]]、[[t-memory-updating]]；矛盾：[[syn-contradictions]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-cohn-2015-coordinated-neuromodulation]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]
