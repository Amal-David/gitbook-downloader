"""Unit tests for is_different_version_path function."""
import pytest
from gitbook_downloader import is_different_version_path


class TestIsDifferentVersionPath:
    """Test cases for version path detection."""

    # Base case: neither URL has version pattern
    def test_no_version_patterns_returns_false(self):
        assert is_different_version_path("https://docs.example.com/guide", "https://docs.example.com/") is False

    # URL has version, base doesn't -> True
    def test_url_has_version_base_does_not(self):
        assert is_different_version_path("https://docs.example.com/v2/guide", "https://docs.example.com/") is True

    # Base has version, URL doesn't -> True
    def test_base_has_version_url_does_not(self):
        assert is_different_version_path("https://docs.example.com/guide", "https://docs.example.com/nightly/") is True

    # Both have version patterns -> False (same version context)
    def test_both_have_version_patterns(self):
        assert is_different_version_path("https://docs.example.com/v2/guide", "https://docs.example.com/v1/") is False

    # Semantic version patterns
    def test_semantic_version_v1(self):
        assert is_different_version_path("https://docs.example.com/v1/guide", "https://docs.example.com/") is True

    def test_semantic_version_v2_0(self):
        assert is_different_version_path("https://docs.example.com/v2.0/guide", "https://docs.example.com/") is True

    def test_semantic_version_v1_2_3(self):
        assert is_different_version_path("https://docs.example.com/v1.2.3/guide", "https://docs.example.com/") is True

    # Named version patterns (existing patterns that should still work)
    def test_nightly_pattern(self):
        assert is_different_version_path("https://docs.example.com/nightly/guide", "https://docs.example.com/") is True

    def test_canary_pattern(self):
        assert is_different_version_path("https://docs.example.com/canary/guide", "https://docs.example.com/") is True

    def test_next_pattern(self):
        assert is_different_version_path("https://docs.example.com/next/guide", "https://docs.example.com/") is True

    def test_latest_pattern(self):
        assert is_different_version_path("https://docs.example.com/latest/guide", "https://docs.example.com/") is True

    def test_testnet_pattern(self):
        assert is_different_version_path("https://docs.example.com/testnet/guide", "https://docs.example.com/") is True

    # New patterns that should be detected
    def test_stable_pattern(self):
        assert is_different_version_path("https://docs.example.com/stable/guide", "https://docs.example.com/") is True

    def test_beta_pattern(self):
        assert is_different_version_path("https://docs.example.com/beta/guide", "https://docs.example.com/") is True

    def test_alpha_pattern(self):
        assert is_different_version_path("https://docs.example.com/alpha/guide", "https://docs.example.com/") is True

    def test_rc_pattern(self):
        assert is_different_version_path("https://docs.example.com/rc/guide", "https://docs.example.com/") is True

    def test_rc1_pattern(self):
        assert is_different_version_path("https://docs.example.com/rc1/guide", "https://docs.example.com/") is True

    def test_dev_pattern(self):
        assert is_different_version_path("https://docs.example.com/dev/guide", "https://docs.example.com/") is True

    def test_staging_pattern(self):
        assert is_different_version_path("https://docs.example.com/staging/guide", "https://docs.example.com/") is True

    def test_main_pattern(self):
        assert is_different_version_path("https://docs.example.com/main/guide", "https://docs.example.com/") is True

    def test_master_pattern(self):
        assert is_different_version_path("https://docs.example.com/master/guide", "https://docs.example.com/") is True

    def test_trunk_pattern(self):
        assert is_different_version_path("https://docs.example.com/trunk/guide", "https://docs.example.com/") is True

    def test_edge_pattern(self):
        assert is_different_version_path("https://docs.example.com/edge/guide", "https://docs.example.com/") is True

    def test_unstable_pattern(self):
        assert is_different_version_path("https://docs.example.com/unstable/guide", "https://docs.example.com/") is True

    # False positive prevention - these should NOT match
    def test_canaries_not_false_positive(self):
        """'canaries' should not match 'canary' pattern."""
        assert is_different_version_path("https://docs.example.com/canaries/guide", "https://docs.example.com/") is False

    def test_nextjs_not_false_positive(self):
        """'nextjs' should not match 'next' pattern."""
        assert is_different_version_path("https://docs.example.com/nextjs/guide", "https://docs.example.com/") is False

    def test_latest_archive_not_false_positive(self):
        """'latest-archive' should not match 'latest' pattern."""
        assert is_different_version_path("https://docs.example.com/latest-archive/guide", "https://docs.example.com/") is False

    def test_development_docs_not_false_positive(self):
        """'development-docs' should not match 'dev' pattern."""
        assert is_different_version_path("https://docs.example.com/development-docs/guide", "https://docs.example.com/") is False

    def test_mainframe_not_false_positive(self):
        """'mainframe' should not match 'main' pattern."""
        assert is_different_version_path("https://docs.example.com/mainframe/guide", "https://docs.example.com/") is False

    def test_masterclass_not_false_positive(self):
        """'masterclass' should not match 'master' pattern."""
        assert is_different_version_path("https://docs.example.com/masterclass/guide", "https://docs.example.com/") is False

    # Case insensitivity
    def test_case_insensitive_nightly(self):
        assert is_different_version_path("https://docs.example.com/NIGHTLY/guide", "https://docs.example.com/") is True

    def test_case_insensitive_v2(self):
        assert is_different_version_path("https://docs.example.com/V2/guide", "https://docs.example.com/") is True

    # Version at end of path (no trailing content)
    def test_version_at_end_of_path(self):
        assert is_different_version_path("https://docs.example.com/docs/v2", "https://docs.example.com/") is True

    # Deeply nested version paths
    def test_deeply_nested_version(self):
        assert is_different_version_path("https://docs.example.com/api/docs/v2/reference", "https://docs.example.com/") is True
