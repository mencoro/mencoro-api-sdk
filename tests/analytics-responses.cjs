const assert = require('node:assert/strict');
const { AnalyticsApi, TrackedQueriesApi, Configuration } = require('../typescript/dist');

const responses = {
  getProjectMetrics: { mentionCount: 6, avgMentionPosition: 3.5, positivityIndex: null,
    sentimentPositive: 3, sentimentNeutral: 2, sentimentNegative: 1,
    aiTrackedQueryCount: 2, aiQueriesWithMention: 2, serpTrackedQueryCount: 0,
    serpQueriesWithResult: 0, shoppingTrackedQueryCount: 0, shoppingQueriesWithResult: 0,
    mentionTypeCounts: { recommendation: 6, comparison: 0, listing: 0, example: 0, reference: 0 },
    mentionPositionDistribution: [], serpPositionDistribution: [], shoppingPositionDistribution: [],
    competitorShareOfVoice: [], dataDirtySince: null },
  getProjectTimeSeries: { points: [{ rawDate: '2026-09-20',
    brand: { mention: 3.5, positivity: null }, competitors: {} }], dataDirtySince: null },
  getTrackedQueryTimeSeries: { points: [], dataDirtySince: null },
  getProjectSentiment: { perEngine: [{ engine: 'chatgpt', positive: 3, neutral: 2,
    negative: 1, mentionCount: 6, positivityIndex: 67 }], perCompetitor: [] },
  getMentionMix: { byType: { recommendation: 6 }, byTone: { positive: 3, neutral: 2, negative: 1 },
    byQualifier: { direct: 6, conditional: 0 } },
  getClusterBreakdown: { rows: [], dataDirtySince: null },
  getCompetitorCoOccurrence: { competitors: [] },
  getQueryMovers: { rows: [], total: 0, dataDirtySince: null },
  getMentionSamples: { samples: [], total: 0 },
  getCitedSources: { sources: [], total: 0 },
};

async function main() {
  for (const [method, payload] of Object.entries(responses)) {
    let called = false;
    const api = new AnalyticsApi(new Configuration({
      accessToken: 'test-key',
      fetchApi: async (url, init) => {
        called = true;
        assert.equal(init.headers.Authorization, 'Bearer test-key');
        return new Response(JSON.stringify(payload), {
          status: 200, headers: { 'Content-Type': 'application/json' },
        });
      },
    }));
    const result = await api[method]({ organizationId: 'org', projectId: 'project',
      trackedQueryId: 'query', dateFrom: new Date('2026-09-20'), dateTo: new Date('2026-09-21') });
    assert.ok(called, method);
    assert.ok(result !== undefined, `${method} discarded the successful JSON response`);
    assert.deepEqual(JSON.parse(JSON.stringify(result)), payload, method);
  }
  for (const [method, suffix] of [
    ['searchTrackedQueryMentionMatches', 'mention-matches'],
    ['searchTrackedQuerySerpMatches', 'serp-matches'],
  ]) {
    const payload = { items: [], total: 12 };
    const api = new TrackedQueriesApi(new Configuration({
      accessToken: 'test-key',
      fetchApi: async (url, init) => {
        assert.ok(new URL(url).pathname.endsWith(`/tracked-queries/query/${suffix}`));
        assert.equal(init.headers.Authorization, 'Bearer test-key');
        return new Response(JSON.stringify(payload), {
          status: 200, headers: { 'Content-Type': 'application/json' },
        });
      },
    }));
    const result = await api[method]({ organizationId: 'org', projectId: 'project',
      trackedQueryId: 'query', offset: 12 });
    assert.deepEqual(result, payload, method);
  }
  console.log('10 analytics operations and 2 match readers preserve their response bodies');
}

main().catch(error => { console.error(error); process.exitCode = 1; });
