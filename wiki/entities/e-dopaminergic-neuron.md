---
title: 多巴胺神經元（dopaminergic neuron, DAN）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# 多巴胺神經元（dopaminergic neuron, DAN）

## 是什麼

釋放多巴胺（dopamine）的神經元。在蘑菇體學習的模型裡，DAN 把「剛剛發生了壞事或好事」送進 [[e-mushroom-body]]：它的軸突末梢伸到 [[e-kenyon-cell]]（KC）與 [[e-mbon]]（MBON）之間的突觸旁，每一型 DAN 只支配葉上的一個或幾個區室（[[c-mb-compartment]]）。

三篇提到兩群與蘑菇體有關的 DAN（以細胞體所在的位置命名的細胞群）：

| 細胞群 | 來源怎麼描述 |
|---|---|
| **PPL1**（Hige 2015 的寫法）／**PPL**（Handler 2019 的寫法） | 傳遞懲罰。傳統的學習實驗用電擊當懲罰；Hige 2015 引文獻說，熱遺傳（讓神經元帶溫度敏感通道、升溫使其放電）活化 PPL1-γ1pedc 可取代電擊；Handler 2019 說 PPL 足以驅動嫌惡記憶 |
| **PAM** | Handler 2019：多報告獎賞。Hige 2015 只在 TH-GAL4 的圖說中提到「少數 PAM DAN」，沒有說明功能 |

※ 推論：PPL1 與 PPL 指同一群。依據是兩篇都把它描述為傳遞懲罰的 DAN 群，且兩篇的驅動品系都用到 TH（合成多巴胺的酵素酪胺酸羥化酶）的調控序列；但兩篇都沒有說明兩個名稱的關係：？待查。

## 庫內誰用了它

| 來源 | 怎麼讓多巴胺出現 | 用到的 DAN 與驅動品系 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **沒有活化 DAN。** 直接把多巴胺加進灌流液（浴灌，10 nM–10 mM），或用玻璃細管噴在垂直葉（細管內 1 mM） | 無。只引 Mao & Davis 2009 說明多巴胺神經元支配蘑菇體 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 光遺傳：DAN 表現 [[e-cschrimson]]，紅光一照就放電 | **PPL1-γ1pedc**（舊名 MB-MP1），由 MB320C 標記，只標這一顆；**MB099C** 標四型 PPL1（γ2α′1、α′2α2、α′3、α3），從不標 PPL1-γ1pedc；**TH-GAL4** 標多數 PPL1（含 γ1pedc）、少數 PAM 與蘑菇體以外的許多 DAN，當正對照（已知應該有效的組，用來確認方法本身有用） |
| [[s-handler-2019-dopamine-receptor-timing]] | 行為：光遺傳（CsChrimson；閉迴路實驗用 ChrimsonR。閉迴路＝果蠅頭固定在顯微鏡下、腳踩泡沫球，球的轉動帶動送氣管，可同時看腦與行為）；離體腦：化學遺傳，DAN 表現 ATP 門控通道 P2X2，滴 ATP 使其放電；另有一組用真的電擊（補充圖 S3E：？待查） | **PAM**：MB042B（行為、閉迴路）、R58E02-LexA（離體；基因型表標為「γ4–5 DANs」）；**PPL**：MB504B（行為，論文說它支配六個區室，沒列出是哪六個）；γ2 DAN：73F07-LexA（補充圖 S3D）；TH-Gal4 加 DDC-Gal4 用來在 DAN 表現 VMAT-pHluorin（見下段） |

品系的專一性問題見 [[e-split-gal4]]。

**Handler 2019 也量了 DAN 本身。** 用 GCaMP6s（DAN 的鈣，約等於放電活動）、VMAT-pHluorin（多巴胺的釋放）與 KC 軸突上的 GRAB_DA1m（KC 收到的多巴胺），發現順向配對（氣味或 KC 刺激在前、DAN 在後）與逆向配對（DAN 在前）時三者都一樣（樣本數見 [[numbers]]）。所以先後次序不是靠「送來多少多巴胺」區分，而是靠 KC 怎麼讀（見 [[c-camp-signaling]]）。

## 已知的問題

- **PPL 與 PAM 的時間規則在 Handler 2019 的行為資料裡不一樣。** Handler 把「DAN 比氣味晚幾秒」從負（DAN 在前）掃到正（DAN 在後），量果蠅之後追氣味的變化。PPL 與 PAM 都會在某個時間差上把效果翻成反方向，但翻轉的位置不同：PPL 約在 DAN 晚 0.49 s、PAM 約在 DAN 早 0.44 s，相差約 0.9 s（以相鄰兩點線性內插，本庫推算，見 [[numbers]]）。0 秒落在 PPL 翻轉點（+0.49 s）之前、PAM 翻轉點（−0.44 s）之後，所以氣味與 DAN 同時開始時，PPL 給的效果和它的逆向配對同方向，PAM 給的效果卻和它的順向配對同方向。論文的分子實驗只做了 PAM→γ4（見 [[t-timing-rules]]）。
- **Hige 2015 只活化 PPL1**（TH-GAL4 那組另含少數 PAM），只看到突觸變弱；獎賞 DAN 會讓突觸往哪個方向變，該篇沒有測。
- **「活化 DAN」不等於「真的懲罰或獎賞」。** 光遺傳與 ATP 都是人工刺激，見 [[c-us-substitution]]。Tomchik 2009 更是連 DAN 都沒動，濃度也不等於組織內的實際濃度。
- **品系涵蓋的範圍沒有完整列出**：MB504B 的六個區室、MB042B 涵蓋哪些區室，Handler 2019 都沒列出；行為結果因此可能來自 γ4 以外的區室。

## 相關

- 結構與細胞：[[e-mushroom-body]]、[[e-kenyon-cell]]、[[e-mbon]]
- 工具：[[e-split-gal4]]、[[e-cschrimson]]、[[e-gcamp]]
- 概念：[[c-us-substitution]]、[[c-cs-us-timing]]、[[c-mb-compartment]]、[[c-camp-signaling]]
- 主題：[[t-timing-rules]]、[[t-dopamine-to-plasticity]]；矛盾：[[syn-contradictions]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]
