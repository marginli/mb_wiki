---
title: 表現指數（performance index, P.I.）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, mb-learning]
confidence: medium
---

# 表現指數（performance index, P.I.）

**表現指數是嗅覺學習行為測驗的分數：訓練後讓一群果蠅在兩個氣味之間選擇，把選擇的分布換算成一個數字，代表這群果蠅學到了多少。** 分數的絕對值越大表示越多果蠅避開（或趨近）被訓練的氣味；分數接近 0 表示選擇與隨機無異。**正值代表「躲」還是「靠近」，各篇約定不同**，引用前一定要先查（見下表與陷阱 2）。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **DAN**：多巴胺神經元（dopaminergic neuron），送出代表懲罰或獎賞的多巴胺。
- **光**：指光遺傳活化 DAN，即讓 DAN 帶上照紅光就放電的蛋白，用光代替真的懲罰或獎賞（見 [[c-us-substitution]]）。
- **CS+、CS−**：CS 是條件刺激（conditioned stimulus），本庫都是氣味。CS+ 是訓練時配了懲罰或獎賞的氣味，CS− 是沒配、當比較基準的另一個氣味。
- **T 迷宮、競技場**：兩種測驗裝置。T 迷宮讓果蠅從中央選左右兩臂之一，各接一種氣味（[[e-t-maze]]）；四象限競技場是圓形小室，對角象限吹同一種氣味（[[e-olfactory-arena]]）。

## 怎麼算 / 怎麼判定

一般形式是「選 A 的果蠅數減選 B 的果蠅數，除以總數」，所以落在 −1 到 +1 之間。差別在 A 是哪一個氣味、有沒有改號，以及有沒有把公式寫出來：

| 來源 | 裝置 | 公式（原文有寫才列） | 正值代表 |
|---|---|---|---|
| Tomchik 2009 | T 迷宮 | 未寫；正文只定義 P.I.＝0 為 50:50、P.I.＝1 為全部選對（避開 CS+） | 避開 CS+ |
| Hige 2015 | 競技場 | 只在補充資料：？待查 | 相對迴避受測氣味 |
| Aso 2016 | 競技場 | 〔（氣味 A 象限隻數）−（氣味 B 象限隻數）〕／總隻數，A＝配光的氣味；取測驗最後 30 s 平均；A、B 互換兩群取平均 | 趨近配光氣味（圖 1、4）；圖 2、3 把嫌惡型品系**改號**，正值＝學到了 |
| Ichinose 2015 | T 迷宮 | 稱學習指數（learning index, LI）：取 2 分鐘選擇的最後 60 s 算偏好指數，互為對照的兩組取平均；偏好指數的換算公式未寫 | 選配過糖的氣味 |
| Felsenberg 2017 | T 迷宮 | 未寫，「如文獻 17（Krashes & Waddell 2008）所述」 | 偏向 CS+（獎賞） |
| Felsenberg 2018 | T 迷宮 | （CS+ 臂隻數 − CS− 臂隻數）÷ 總數（引 Tully & Quinn 1985）；MCH、OCT 輪流當 CS+，兩組平均為一個 n | 偏向 CS+；本篇是電擊訓練，所以**躲 CS+ 時為負值** |

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-tomchik-2009-camp-dynamics]] | 量 trace 制約的行為時間窗，與 cAMP 協同的時間窗並列 | 氣味與電擊同時給約 0.72；倒序（電擊先）約 0.04；trace（氣味結束後空白 0／15／30／45 s 才電擊）約 0.47／0.22／0.13／0.05；n＝6 |
| [[s-hige-2015-heterosynaptic-plasticity]] | 量學到的迴避會不會類化到相似氣味（[[c-odor-generalization]]） | PA 與光配對約 67、不配對（光與 PA 錯開給的對照組）約 5；BA 約 42 vs 9；HP 約 38 vs −2；每組 n＝10 |
| [[s-aso-2016-dan-cell-type-rules]] | 同一群果蠅在競技場裡反覆訓練與測驗；比較六組 DAN 品系的學習速率、保留、削弱、容量 | 單一 DAN（MB320C）的時間差掃描：嫌惡最低約 −0.45、逆向 20–60 s 喜好約 +0.15；對照組約 0.07 與 −0.01 |
| [[s-ichinose-2015-reward-recurrent-circuit]] | 以 LI 比較阻斷或降低受體後的 5 分鐘與 24 小時記憶 | 例：活化 MBON-α1 代替糖，24 h LI 約 0.15，真糖訓練的對照多在 0.3–0.45 |
| [[s-felsenberg-2017-re-evaluation]] | 糖獎賞記憶再聞 CS+ 或 CS− 後，6 小時的 PI | 消退後約 0.01，其他組約 0.2–0.3（見 [[c-memory-extinction]]） |
| [[s-felsenberg-2018-memory-extinction]] | 電擊記憶再聞 CS+ 後，1 小時的 P.I. | 例：不再暴露約 −0.39、再聞 CS+ 兩次約 −0.20，躲避少了約一半 |

> 數值皆為從圖判讀，見 [[numbers]] 與各來源頁。**Handler 2019 不用 P.I.**（全文 grep `performance` 無結果）：它的行為指標是一盒 4–7 隻果蠅的群體重心在 2 s 氣味期間往上風（氣味源）移動的距離（mm）；正值＝往氣味走＝吸引。Cohn 2015 沒有任何行為選擇測驗。

## 引用時的陷阱

1. **刻度不同。** Tomchik 2009、Aso 2016、Felsenberg 兩篇的值落在 −1 到 +1；Hige 2015 圖上的值在數十，上下限與換算方式都 ？待查。跨篇不要直接比數值。
2. **正負號至少有三種約定。** 正值＝躲 CS+（Tomchik 2009、Hige 2015）；正值＝偏向 CS+，所以電擊記憶為負（Felsenberg 2018）；正值＝偏向配過獎賞的 CS+（Felsenberg 2017、Ichinose 2015）。Aso 2016 同一篇裡圖 1、4 未改號（負＝躲）、圖 2、3 改號（正＝學到）。Handler 2019 的位移正值＝吸引。並列時要先對齊方向。
3. **n 是「群」不是「隻」。** P.I. 是一群果蠅算出一個數（Felsenberg 2017 每群 50–100 隻，Aso 2016 約 20 隻）；Tomchik 2009 的 n＝6 是 6 次 P.I.。Aso 2016 的 N 是一群還是一對互換群，PDF 沒說：？待查。
4. **行為與生理常不是同一批果蠅。** Hige 2015 的 PI 與突觸記錄來自不同果蠅、不同光協定；Felsenberg 2018 的成像組在顯微鏡下訓練，與行為組不是同一批。
5. **「降到 0」有兩種讀法。** 二選一的分數是兩個氣味記憶的差。Felsenberg 2017 再聞 CS− 後 PI 歸零，可能是忘了 CS+，也可能是對 CS− 也產生了偏好；該篇只在一個操作上改用新氣味對照來分辨（圖 2f）。Aso 2016 圖 3E 的低分也同樣分不出「新記憶學不起來」與「新舊相抵」。

## 相關

- 主題：[[t-timing-rules]]、[[t-memory-updating]]
- 概念：[[c-cs-us-timing]]、[[c-us-substitution]]、[[c-memory-extinction]]、[[c-odor-generalization]]
- 實體：[[e-t-maze]]、[[e-olfactory-arena]]
- 來源：[[s-tomchik-2009-camp-dynamics]]、[[s-hige-2015-heterosynaptic-plasticity]]、[[s-aso-2016-dan-cell-type-rules]]、[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-felsenberg-2018-memory-extinction]]、[[s-handler-2019-dopamine-receptor-timing]]
