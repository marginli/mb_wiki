---
title: 全細胞膜片鉗記錄（whole-cell patch clamp）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, cross-domain]
confidence: high
---

# 全細胞膜片鉗記錄（whole-cell patch clamp）

**把尖端極細的玻璃電極貼上一顆神經元的細胞膜、再把那一小塊膜打穿，讓電極直接接觸細胞內部，就能量到這顆細胞的電位變化或流進來的電流。** 它能逐毫秒看到單一神經元的放電（尖峰）與突觸電流，比螢光鈣影像更直接；代價是一次只能記一顆細胞，且要找得到、接得上那顆細胞。本庫用它量 KC→MBON 突觸在多巴胺作用後變強還是變弱。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體、KC、葉、區室**：蘑菇體（mushroom body）是果蠅腦中把氣味和好壞經驗連起來的構造；代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」，每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ4、α1），細胞以所在區室命名（見 [[e-mushroom-body]]、[[c-mb-compartment]]）。
- **常見詞**：PAM／PPL1＝兩群多巴胺神經元（DAN），分別多傳遞獎賞／懲罰；光遺傳＝讓神經元帶上照光就放電的蛋白（[[e-cschrimson]]）；離體＝把腦取出泡在養液裡，活體＝活果蠅固定後看腦；順向配對＝氣味先、多巴胺後，逆向＝多巴胺先；「未配對」＝兩種刺激錯開、不同時出現；cAMP＝多巴胺受體被活化後在細胞內產生的訊號小分子；※ 推論＝本庫推得、原文沒明說，？待查＝要靠其他資料確認。
- **MBON、KC、DAN**：蘑菇體輸出神經元、Kenyon 細胞、多巴胺神經元（見 [[e-mbon]]、[[e-kenyon-cell]]、[[e-dopaminergic-neuron]]）。
- **電流箝制**（current clamp）：讓膜電位自由變化，看得到尖峰。
- **電壓箝制**（voltage clamp）：儀器把膜電位固定在設定值，量到的是流入細胞的電流。
- **EPSC**：興奮性突觸後電流，從突觸流進 MBON 的電流；其總量稱電荷（pC）。
- **潛時**（latency）：刺激到電流出現的時間；越短越可能是單一突觸直接傳來。

## 怎麼算 / 怎麼判定

在配對（或單獨活化 DAN）前後各記錄一次同一顆 MBON 對同樣輸入（氣味或 KC 刺激）的反應，比較尖峰數、EPSC 振幅或電荷。定位到 KC→MBON 突觸的常見論證：潛時短（單突觸）、KC 本身的興奮性不變、MBON 不放電也會發生。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-hige-2015-heterosynaptic-plasticity]] | 活體、頭部固定；記錄 MBON-γ1pedc、MBON-α2sc、MBON-γ2α′1；電流箝制看尖峰，電壓箝制（含銫內液＋10 mM QX-314 消除 MBON 自身尖峰，維持 −70 或 −60 mV）看 EPSC；部分以 cell-attached（不打穿膜、只量尖峰）代替 | 配對氣味的放電降 80% ± 5.7%、EPSC 電荷降 90% ± 3.7%；電壓箝制下配對（MBON 尖峰被抑 83% ± 4.5%）照樣誘發減弱 → 不需要突觸後放電 |
| [[s-cohn-2015-coordinated-neuromodulation]] | 離體腦；γ4 MBON 電壓箝制（名義上 −70 mV），刺激為乙醯膽鹼離子導入萼部；另記錄 KC 檢查其電位與放電 | 活化 58E02 DAN 後 γ4 MBON 誘發電流約 1.5 → 16 pA（n＝5，從圖判讀）；EPSC 潛時 3.8 ± 0.1 ms，作者據此判為單突觸；KC 的基礎膜電位與放電不變（補充圖 S6B，？待查） |

> 數值見 [[numbers]] 與 [[c-kc-mbon-plasticity]]。

## 引用時的陷阱

1. **兩篇記錄的條件不同，數值不能並排。** Hige 2015 在活體用真的氣味、量尖峰數與電荷（pC）；Cohn 2015 在離體用乙醯膽鹼、量電流振幅（pA）。Cohn 2015 的其他 MBON 結果（圖 6B–E、7）改用鈣影像，不是膜片鉗。
2. **「九成」是電荷總量。** Hige 2015 的電流起始峰值大致保留，少掉的是之後的持續段。
3. **電壓箝制不一定箝得住。** Cohn 2015 方法說 MBON 自身的動作電位有時壓不住、會混入量測（作者說很少且容易辨認）；Hige 2015 剔除有未箝住尖峰的細胞。
4. **膜片鉗量的是突觸後的一顆細胞，不能直接說明改變在突觸前還是突觸後**（Hige 2015 自陳未定），見 [[c-presynaptic-calcium]] 與 [[t-dopamine-to-plasticity]]。
5. **n 小**：Hige 2015 各實驗 n＝5–8；Cohn 2015 膜片鉗 n＝5。

## 相關

- 概念：[[c-kc-mbon-plasticity]]、[[c-ex-vivo-explant]]、[[c-presynaptic-calcium]]、[[c-mb-compartment]]
- 實體：[[e-mbon-gamma1pedc]]、[[e-mbon-gamma2alpha1]]、[[e-mbon-gamma4]]、[[e-p2x2]]、[[e-cschrimson]]
- 主題：[[t-dopamine-to-plasticity]]
- 來源：[[s-hige-2015-heterosynaptic-plasticity]]、[[s-cohn-2015-coordinated-neuromodulation]]
