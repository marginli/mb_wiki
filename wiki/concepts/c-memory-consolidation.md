---
title: 記憶鞏固與再鞏固（memory consolidation and reconsolidation）
created: 2026-10-25
updated: 2026-10-25
tags: [concept, active, mb-memory-dynamics]
confidence: medium
---

# 記憶鞏固與再鞏固（memory consolidation and reconsolidation）

**剛學到的記憶起初不穩定，要經過訓練後一段時間的處理才變成能撐上一天以上的長期記憶（long-term memory, LTM），這段過程叫鞏固（consolidation）。** 已鞏固的記憶被叫出來（再聞到氣味）時，可能暫時又變得不穩定，要再經過一段時間才重新存好，這叫再鞏固（reconsolidation）。本庫的實驗都用「在某段時間干擾腦，記憶就壞掉」來判定這段時間是否處於不穩定期。

**本頁用語**（每頁可單獨查閱，故重複列出）：

- **蘑菇體、KC、葉、區室**：蘑菇體（mushroom body）是果蠅腦中把氣味和好壞經驗連起來的構造；代表氣味的 Kenyon 細胞（KC）把軸突成束排成幾條「葉」，每條葉沿長度切成一格一格的「區室」（例如 γ1pedc、γ4、α1），細胞以所在區室命名（見 [[e-mushroom-body]]、[[c-mb-compartment]]）。
- **常見詞**：PAM／PPL1＝兩群多巴胺神經元（DAN），分別多傳遞獎賞／懲罰；光遺傳＝讓神經元帶上照光就放電的蛋白（[[e-cschrimson]]）；離體＝把腦取出泡在養液裡，活體＝活果蠅固定後看腦；順向配對＝氣味先、多巴胺後，逆向＝多巴胺先；「未配對」＝兩種刺激錯開、不同時出現；cAMP＝多巴胺受體被活化後在細胞內產生的訊號小分子；※ 推論＝本庫推得、原文沒明說，？待查＝要靠其他資料確認。
- **STM／LTM**：短期／長期記憶；在 Ichinose 2015 分別指訓練後 5 分鐘與 24 小時測得的記憶。
- **CS+／CS−**：訓練時配了糖的氣味／沒配糖的對照氣味。
- **冷休克**（cold shock）：把果蠅放在冰上麻醉 2 分鐘，用來擾亂不穩定的記憶。
- **shibire^ts**：升溫時暫時關掉選定神經元輸出的工具，見 [[e-shibire-ts]]。
- **DAN、MBON、KC**：多巴胺神經元、蘑菇體輸出神經元、Kenyon 細胞（見 [[e-dopaminergic-neuron]]、[[e-mbon]]、[[e-kenyon-cell]]）。

## 怎麼算 / 怎麼判定

- **鞏固**：在訓練後的某個時間窗阻斷某群神經元（或給冷休克），隔天測記憶；早期阻斷傷記憶、晚期阻斷不傷，就判定該時間窗屬於鞏固期、該神經元在鞏固期必要。
- **再鞏固**：訓練、等記憶穩定後再暴露氣味，接著在不同時間點給冷休克或阻斷；再暴露後不久干擾會讓記憶消失、晚一點干擾就不會，即判定為再鞏固。
- **記憶保留**：比較即時、1 日、4 日的分數，看記憶撐多久（Aso 2016 的用法；它量的是保留，不是鞏固過程本身）。

## 庫內的用法

| 來源 | 怎麼用 | 得到什麼 |
|---|---|---|
| [[s-ichinose-2015-reward-recurrent-circuit]] | 糖獎賞一次訓練；以 shi 在訓練時、訓練後立刻 1 h、訓練後 22 h 起 1 h、或測試時阻斷 PAM-α1、MBON-α1、α/β KC | 訓練時或訓練後 0–1 h 阻斷都傷 24 h 記憶，22 h 後阻斷不傷；5 分鐘記憶未顯著受損（但實驗組比一個對照低約四成）；提取需要 MBON-α1、不需要 PAM-α1（後者 n 小）；作者模型「迴圈讓多巴胺在糖拿走後繼續釋放」未直接量過 |
| [[s-felsenberg-2017-re-evaluation]] | 糖獎賞記憶訓練後 3 h（或 21 h）再暴露 CS−（訓練時本來就沒有糖的那個氣味；聞到它「沒有糖」符合預期，作者認為這會叫出記憶卻不引發消退），再在 0／30／90 分鐘給冷休克，或在再暴露期間／之後阻斷 DAN 與 MBON | 0 與 30 分鐘冷休克使 6 h 記憶消失；90 分鐘時約回到未冰組的六成（從圖判讀，與未冰組差異不顯著）；再暴露期間需要 PPL1-γ2α′1（MB-MV1）與 MBON-γ2α′1，再暴露後立刻需要 PAM，90 分鐘後不需要 |
| [[s-aso-2016-dan-cell-type-rules]] | 以單型 DAN 光遺傳訓練，比較即時、1 日、4 日記憶；單次 vs 10 次間隔訓練（見 [[c-spaced-training]]） | MB320C（PPL1-γ1pedc）即時最強但 10 次訓練後仍無 4 日記憶；MB630B（PPL1-α3）即時不顯著、10 次後有 4 日記憶；作者稱記憶穩定度是區室的性質，並說形成與鞏固「與在各區室平行、獨立進行一致」 |

> 數值見 [[numbers]]；鞏固、再鞏固與消退在記憶更新中的關係見 [[t-memory-updating]]，迴路回饋見 [[t-mbon-dan-feedback]]。

## 引用時的陷阱

1. **「需要」是阻斷的結論，不是活動的量測。** Ichinose 2015 的圖題寫「dopamine release」，全篇沒有量多巴胺或神經活動；Felsenberg 2017 也沒有在活果蠅再暴露時量 DAN 活動。
2. **shi 的時間解析度粗。** Felsenberg 2017 從再暴露前 30 分鐘就升溫，所以「期間 vs 之後」的區分約以數十分鐘計；Ichinose 2015 訓練時阻斷維持多久論文沒寫。
3. **「不顯著」常被讀成「沒作用」。** Felsenberg 2017 的 90 分鐘冷休克組、再暴露後才阻斷 MB-MV1 的組（下降約兩到三成、n ≥ 23 仍不顯著），Ichinose 2015 的 STM 組都是如此。
4. **再鞏固的判準只有冷休克與阻斷。** Felsenberg 2017 沒有做蛋白質合成抑制（已 grep cycloheximide、protein synthesis，只在參考文獻標題）。
5. **Aso 2016 量的是保留，不是鞏固過程。** 它沒有在訓練後的時間窗做干擾；「穩定度是區室的性質」的比較來自不同驅動品系，活化強度未校準。
6. **三篇的「長期」不同**：Ichinose 24 h、Felsenberg 2017 測 6 h（再暴露在 3 h）、Aso 1 日與 4 日。

## 相關

- 主題：[[t-memory-updating]]、[[t-mbon-dan-feedback]]
- 概念：[[c-memory-extinction]]、[[c-spaced-training]]、[[c-performance-index]]
- 實體：[[e-shibire-ts]]、[[e-t-maze]]、[[e-pam-alpha1]]、[[e-ppl1-gamma2alpha1]]、[[e-mbon-gamma2alpha1]]、[[e-dopamine-receptor]]
- 來源：[[s-ichinose-2015-reward-recurrent-circuit]]、[[s-felsenberg-2017-re-evaluation]]、[[s-aso-2016-dan-cell-type-rules]]
