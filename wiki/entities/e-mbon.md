---
title: 蘑菇體輸出神經元（mushroom body output neuron, MBON）
created: 2026-10-25
updated: 2026-10-25
tags: [entity, active, mb-learning]
confidence: medium
---

# 蘑菇體輸出神經元（mushroom body output neuron, MBON）

## 是什麼

讀取 [[e-kenyon-cell]]（KC）訊號、再把結果送出 [[e-mushroom-body]] 去影響行為的神經元。每型 MBON 的樹突佔據葉上的一個區室（[[c-mb-compartment]]），在那裡收 KC 軸突送來的訊號；同一區室裡另有一型 [[e-dopaminergic-neuron]]（DAN）調整這個「KC → MBON」突觸的強弱。MBON 以所在區室命名，例如 MBON-γ1pedc 的樹突在 γ1pedc 區室。

**價值（valence）**：直接活化不同的 MBON，會讓果蠅靠近或走開。Hige 2015 與 Handler 2019 都引 Aso et al. 2014b 說明這件事；Hige 2015 另引該文說，一般而言 MBON 推動的行為方向，與同區室 DAN 傳遞的價值相反（例如懲罰 DAN 配推動靠近的 MBON）。因此學到「這個氣味不好」，就是把推動靠近的 MBON 對該氣味的反應壓低。

## 庫內誰用了它

| 來源 | 記錄的 MBON | 推動靠近或走開（依來源所引） | 怎麼量 | 看到什麼 |
|---|---|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | **未量 MBON** | — | — | 只量 KC 內部；KC→MBON 突觸是否改變，本篇無從回答 |
| [[s-hige-2015-heterosynaptic-plasticity]] | **γ1pedc**（舊名 MB-MVP2，R12G04-LexA 讓它帶綠色螢光蛋白 GFP，方便電極對準）；**α2sc**（R34B02-LexA）；**γ2α′1**（R25D01-LexA） | γ1pedc：靠近（引 Aso 2014b）。α2sc、γ2α′1：該篇未說明，？待查 | 活體全細胞膜片鉗（把玻璃電極接上細胞、直接量細胞內的電訊號）：記錄放電次數（尖峰數）與從突觸流進來的電流（興奮性突觸後電流，EPSC；其累積總量稱電荷，單位 pC） | γ1pedc：氣味配 DAN 一次，突觸長期變弱（長期抑制，LTD）；α2sc：要 1 分鐘的配對才變弱；在 γ1 區配對、讓 γ1 突觸變弱時，鄰區的 γ2α′1 不變 |
| [[s-handler-2019-dopamine-receptor-timing]] | **γ4**（主力；離體 VT026001-Gal4，在體 R53C03-LexA）；**γ2**（25D01-Gal4／25D01-LexA）、**γ5**（66C08-Gal4），兩者在補充圖 S3：？待查 | γ2：靠近；γ4、γ5：走開（皆引 Aso 2014b） | GCaMP6s（[[e-gcamp]]）量區室內樹突的鈣反應 | γ4：多巴胺在後→變弱，多巴胺在前→變強（雙向）；論文說 γ2、γ5 也有類似的雙向改變 |

數字（降幅、n、協定）見 [[numbers]] 與 [[c-kc-mbon-plasticity]]。

※ 推論：Handler 2019 的「γ2 MBON」與 Hige 2015 的 MBON-γ2α′1 可能是同一型細胞。依據是兩篇標記它用的都是 25D01 這段調控序列（Hige：R25D01-LexA；Handler：25D01-Gal4 與 25D01-LexA）。不確定之處：同一段序列做成 GAL4 與 LexA 品系，標到的細胞不一定完全相同，兩篇也都沒有比對：？待查。

## 已知的問題

- **逆向配對的結果兩篇不同。** Hige 2015 的 γ1pedc：先用光活化 DAN、再給氣味（即多巴胺在前），突觸不變；Handler 2019 的 γ4：多巴胺在前，突觸變強。兩篇的區室、DAN、製備、時間間隔都不同，本頁不裁決，見 [[syn-contradictions]] 1.1。
- **讀出方式不同，數值不能並排。** Hige 用電極量尖峰數與電荷（pC），Handler 用鈣影像的 ΔF/F（螢光相對基線的變化比例）。「降九成」與「ΔF/F 從 1.22 降到 0.42」不是同一種量。
- **「推動靠近或走開」都是引用 Aso 2014b**，兩篇都沒有自己檢驗所記錄 MBON 的行為效果。
- **行為由多個區室合成。** Hige 只量 γ1pedc 一個區室就對照整隻果蠅的類化行為（學會躲一種氣味後，也躲相似的氣味）；Handler 也承認行為不只來自 γ4。

## 相關

- 細胞：[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]；結構：[[e-mushroom-body]]
- 工具：[[e-gcamp]]、[[e-split-gal4]]、[[e-cschrimson]]
- 概念：[[c-kc-mbon-plasticity]]、[[c-mb-compartment]]、[[c-cs-us-timing]]
- 主題：[[t-dopamine-to-plasticity]]、[[t-timing-rules]]；矛盾：[[syn-contradictions]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-handler-2019-dopamine-receptor-timing]]、[[s-tomchik-2009-camp-dynamics]]
